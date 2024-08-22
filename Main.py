import matplotlib.pylab as plt
from API import transfer_style
import os

if __name__ == "__main__":

    # Assuming the script is running from the 'Neural-Style-Transfer' directory

    # Path of the pre-trained TF model 
    model_path = os.path.join(os.getcwd(), "model")

    # NOTE: Works only for '.jpg' and '.png' extensions, other formats may give error
    content_image_path = os.path.join(os.getcwd(), "Imgs", "stevejobs2.jpg") # Orignal Image
    style_image_path = os.path.join(os.getcwd(), "Imgs", "style7.jpg") # Styling Image

    img = transfer_style(content_image_path, style_image_path, model_path)
    
    # Saving the generated image
    plt.imsave('stylized_image.jpeg', img)
    plt.imshow(img)
    plt.show()
