import matplotlib.pylab as plt
from api import transfer_style
import os

if __name__ == "__main__":

    # Assuming the script is running from the 'Neural-Style-Transfer' directory

    # Path of the pre-trained TF model 
    model_path = os.path.join(os.getcwd(), "model")

    # NOTE: Works only for '.jpg' and '.png' extensions, other formats may give error
    content_image_path = os.path.join(os.getcwd(), "Imgs", "bluemoonlake.jpg") # Orignal Image
    style_image_path = os.path.join(os.getcwd(), "Imgs", "style1.jpg") # Styling Image

    img = transfer_style(content_image_path, style_image_path, model_path)

    # # Looping through all the style images
    # for i in range(1, 19):
    #         style_image_path = os.path.join(os.getcwd(), "Imgs", f"style{i}.jpg")  # Styling Image

    #         # Check if the style image exists
    #         if not os.path.exists(style_image_path):
    #             print(f"Style image {i} not found at {style_image_path}")
    #             continue

    #         try:
    #             # Apply style transfer
    #             img = transfer_style(content_image_path, style_image_path, model_path)
                
    #             # Saving the generated image
    #             output_image_path = f'stylized_image_{i}.jpeg'
    #             plt.imsave(output_image_path, img)
                
    #             # Display the generated image
    #             plt.imshow(img)
    #             plt.title(f'Style {i}')
    #             plt.show()
    #         except Exception as e:
    #             print(f"Error processing style image {i}: {e}")

    # Saving the generated image
    plt.imsave('stylized_image.jpeg', img)
    plt.imshow(img)
    plt.show()
