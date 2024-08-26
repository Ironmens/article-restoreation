# Visualization code
import matplotlib.pyplot as plt
import os
import cv2
def plot_single_image(img_file_path, title):
  # Load and display the image
  img_bgr = cv2.imread(img_file_path)
  img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
  plt.imshow(img_rgb)
  plt.axis('off')  # Hide axes
  plt.title(title)  # Set the title of the plot
  plt.show()

def visualize_output(input_img_file, output_dir):
  item_dir = os.listdir(output_dir)[0]
  item_res_dir = os.path.join(output_dir, item_dir, 'results')

  final_output_file = os.path.join(item_res_dir, 'final_output.png')
  plot_single_image(input_img_file, title='Input Image')
  plot_single_image(final_output_file, title='Edited Image')

plot_single_image('images/1.png', title='Input Image')

print('Editing prompt:', 'a big tree with many flowers in the center')
visualize_output('images/1.png', 'output')