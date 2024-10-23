# Import necessary libraries
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os
import csv  # For writing to CSV

# File paths for the images
base_image_path = r"D:\Academics\EN3160 - Image Processing and Machine Vision\assignments\Assignment_02\images\building.jpg"
imposing_image_path = r"D:\Academics\EN3160 - Image Processing and Machine Vision\assignments\Assignment_02\images\flag.png"

# Check if the base image exists before attempting to load it
if not os.path.exists(base_image_path):
    print(f"Error: The file {base_image_path} was not found.")
else:
    # Load and convert base image if the file exists
    base_img = cv.imread(base_image_path)
    if base_img is None:
        print(f"Error: Failed to load the image {base_image_path}.")
    else:
        base_img = cv.cvtColor(base_img, cv.COLOR_BGR2RGB)

        # Load and convert imposing image (do the same check)
        if not os.path.exists(imposing_image_path):
            print(f"Error: The file {imposing_image_path} was not found.")
        else:
            imposing_img = cv.imread(imposing_image_path)
            if imposing_img is None:
                print(f"Error: Failed to load the image {imposing_image_path}.")
            else:
                imposing_img = cv.cvtColor(imposing_img, cv.COLOR_BGR2RGB)

                # List to store coordinates of the points clicked by the user
                user_clicked_points = []

                # Function to handle mouse click events on the displayed image
                def handle_click(event):
                    # Get the x and y coordinates from the click event
                    x_coord, y_coord = event.xdata, event.ydata

                    # Check if valid coordinates were clicked inside the image axes
                    if x_coord is not None and y_coord is not None:
                        # Store the clicked point as integers in the list
                        user_clicked_points.append((int(x_coord), int(y_coord)))

                        # Mark the clicked point on the image with a red dot
                        plt.scatter(int(x_coord), int(y_coord), color='red')
                        plt.gcf().canvas.draw()

                        # Print the coordinates to the console
                        print(f'Clicked location: x = {int(x_coord)}, y = {int(y_coord)}')

                # Connect the figure canvas to the click event handler function
                click_event_id = plt.gcf().canvas.mpl_connect('button_press_event', handle_click)

                # Display the image and keep the window open until it is closed manually
                plt.imshow(base_img)
                plt.show()

                # Saving clicked points to a CSV file as integers
                output_file_path = os.path.join(r"D:\Academics\EN3160 - Image Processing and Machine Vision\assignments\Assignment_02", "clicked_points_Q3_1.csv")
                with open(output_file_path, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(['x', 'y'])  # Header row
                    writer.writerows(user_clicked_points)
                
                print(f"All clicked points have been saved to {output_file_path}.")