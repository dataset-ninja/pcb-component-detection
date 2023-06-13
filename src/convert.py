import os

import supervisely as sly
from supervisely.io.fs import dir_exists, file_exists, get_file_name


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    dataset_path = "/Users/iwatkot/Downloads/ninja-datasets/pcb"

    batch_size = 30

    # train_images_folder = "train"
    images_folder = "images"
    bboxes_folder = "labels"
    # val_images_folder = "validation"
    # test_images_folder = "test"
    classes_names = [
        "Cap1",
        "Cap2",
        "Cap3",
        "Cap4",
        "MOSFET",
        "Mov",
        "Resestor",
        "Resistor",
        "Transformer",
    ]

    def create_ann(image_path):
        labels = []

        mask_name = get_file_name(image_path) + ".txt"
        image_np = sly.imaging.image.read(image_path)[:, :, 0]
        img_height = image_np.shape[0]
        img_wight = image_np.shape[1]
        mask_path = os.path.join(bboxes_path, mask_name)
        if file_exists(mask_path):
            with open(mask_path) as f:
                content = f.read().split("\n")

                for curr_data in content:
                    if len(curr_data) != 0:
                        ann_data = list(map(float, curr_data.split(" ")))
                        curr_obj_class = idx_to_obj_class[int(ann_data[0])]
                        left = int((ann_data[1] - ann_data[3] / 2) * img_wight)
                        right = int((ann_data[1] + ann_data[3] / 2) * img_wight)
                        top = int((ann_data[2] - ann_data[4] / 2) * img_height)
                        bottom = int((ann_data[2] + ann_data[4] / 2) * img_height)
                        rectangle = sly.Rectangle(top=top, left=left, bottom=bottom, right=right)
                        label = sly.Label(rectangle, curr_obj_class)
                        labels.append(label)

        return sly.Annotation(img_size=(img_height, img_wight), labels=labels)

    all_datasets = os.listdir(dataset_path)

    idx_to_obj_class = {}
    for idx, class_name in enumerate(classes_names):
        idx_to_obj_class[idx] = sly.ObjClass(class_name, sly.Rectangle)

    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(obj_classes=list(idx_to_obj_class.values()))
    api.project.update_meta(project.id, meta.to_json())

    for curr_dataset in all_datasets:
        ds_path = os.path.join(dataset_path, curr_dataset)
        if dir_exists(ds_path):
            dataset = api.dataset.create(project.id, curr_dataset, change_name_if_conflict=True)

            images_path = os.path.join(ds_path, images_folder)
            bboxes_path = os.path.join(ds_path, bboxes_folder)
            images_names = os.listdir(images_path)

            progress = sly.Progress("Create dataset {}".format(curr_dataset), len(images_names))

            for img_names_batch in sly.batched(images_names, batch_size=batch_size):
                images_pathes_batch = [
                    os.path.join(images_path, image_name) for image_name in img_names_batch
                ]
                img_infos = api.image.upload_paths(dataset.id, img_names_batch, images_pathes_batch)
                img_ids = [im_info.id for im_info in img_infos]
                anns_batch = [create_ann(image_path) for image_path in images_pathes_batch]
                api.annotation.upload_anns(img_ids, anns_batch)

                progress.iters_done_report(len(img_names_batch))

    return project
