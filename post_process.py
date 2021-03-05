

import customize_obj


if __name__ == '__main__':
    output_folder = 'C:/Users/margr/OneDrive - Norwegian University of Life Sciences/Documents/Master/post process/MED_HOG2_W_A/' 
    # change this to the folder you want to store the result
    
    dataset_file = 'C:/Users/margr/OneDrive - Norwegian University of Life Sciences/Documents/Master/Data/full_dataset_singleclass.h5' 
    # path to the dataset

    predicted_h5 = 'C:/Users/margr/OneDrive - Norwegian University of Life Sciences/Documents/Master/OrionResults/BRUKTE/2d_unet_MED_HOG2_W_A/prediction/prediction.030.h5' 
    # the prediction file you want to calculate the dice

    dice_per_slice = output_folder + 'slice.csv'
    dice_per_patient = output_folder + 'patient.csv'
    merge_file = output_folder + 'merge_images.h5'

    customize_obj.H5MetaDataMapping(
        dataset_file,
        dice_per_slice,
        folds=['val'], # change this to ['test'] if you want to calculate the dice of the test prediction
        fold_prefix='',
        dataset_names=['patient_idx', 'slice_idx']
    ).post_process()

    customize_obj.H5CalculateFScore(
        predicted_h5,
        dice_per_slice
    ).post_process()

    customize_obj.H5Merge2dSlice(
        predicted_h5,
        dice_per_slice,
        map_column='patient_idx',
        merge_file=merge_file,
        save_file=dice_per_patient
    ).post_process()

    customize_obj.H5CalculateFScore(
        merge_file,
        dice_per_patient,
        map_file=dice_per_patient,
        map_column='patient_idx'
    ).post_process()
