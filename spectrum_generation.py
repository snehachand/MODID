import spectral
import numpy as np
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Define the HDR file and binary mask paths
image_path = r"F:\a\MODID\data\173\173.hdr"
mask_path = r"F:\a\MODID\masks\173.png"

# # Load the HDR file and binary mask
image = spectral.open_image(image_path)
mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)

# Get the number of bands from the image
num_bands = image.shape[2] 

# Create an empty array to store the mean band values for the ROI
mean_spectrum = np.zeros(num_bands)

# Loop through each band and calculate the mean value for the ROI
for band in range(num_bands):
    # Extract the spectral data for the current band using boolean indexing
    band_data = image[:, :, band][mask > 0]
    
    # Calculate the mean value for the band
    mean_value = np.mean(band_data)
    
    # Store the mean value in the mean_spectrum array
    mean_spectrum[band] = mean_value

# Plot the mean spectrum
wavelengths = np.arange(len(mean_spectrum))  # Replace with actual wavelength values
plt.plot(wavelengths, mean_spectrum)
plt.xlabel('Wavelength')
plt.ylabel('Mean Spectrum')
plt.title('Mean Spectrum for ROI')
plt.show()