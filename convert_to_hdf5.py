import os
import mne

# Get the current working directory
data_path = os.getcwd()

# List all files in the current directory with the '.set' extension
set_files = [f for f in os.listdir(data_path) if f.endswith('.set')]

# Iterate through each .set file and convert to HDF5
for set_file in set_files:
    # Construct the full path to the .set file
    set_path = os.path.join(data_path, set_file)

    # Read EEG data from the .set file
    eeg_data = mne.io.read_raw_eeglab(set_path, preload=True)

    # Generate a valid HDF5 filename without special characters
    h5_file = set_file.replace('.set', '_converted.fif')
    h5_file = mne.utils._clean_names([h5_file])[0]

    # Save to HDF5 format with the .fif extension
    h5_path = os.path.join(data_path, h5_file)
    eeg_data.save(h5_path, overwrite=True)

    # Close the data to free up resources
    eeg_data.close()

print("Conversion complete.")