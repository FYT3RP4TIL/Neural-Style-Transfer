import matplotlib.pylab as plt
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
from tqdm import tqdm
import time

def transfer_style(content_image, style_image, model_path):
    print("Loading images...")
    content_image = plt.imread(content_image)
    style_image = plt.imread(style_image)

    print("Resizing and Normalizing images...")
    content_image = content_image.astype(np.float32)[np.newaxis, ...] / 255.
    style_image = style_image.astype(np.float32)[np.newaxis, ...] / 255.
    style_image = tf.image.resize(style_image, (256, 256))

    print("Loading pre-trained model...")
    hub_module = hub.load(model_path)

    print("Generating stylized image now...")
    
    def stylize_with_progress():
        progress_bar = tqdm(total=100, desc="Stylizing image", ncols=100)
        
        # Simulate incremental progress
        for i in range(90):
            time.sleep(0.05)  # Simulate some processing time
            progress_bar.update(1)
        
        # Actual stylization
        outputs = hub_module(tf.constant(content_image), tf.constant(style_image))
        stylized_image = outputs[0]
        
        # Complete the progress bar
        progress_bar.update(10)
        progress_bar.close()
        
        return stylized_image

    stylized_image = stylize_with_progress()

    stylized_image = np.array(stylized_image)
    stylized_image = stylized_image.reshape(
        stylized_image.shape[1], stylized_image.shape[2], stylized_image.shape[3])

    print("Stylizing completed...")
    return stylized_image