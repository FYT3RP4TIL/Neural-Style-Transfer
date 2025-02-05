# Neural Style Transfer: Create AI-Generated Art 🎨🖌️

Transform your photos into stunning digital art using the power of Neural Style Transfer!

## 🌟 Overview

Neural Style Transfer (NST) is an innovative AI technique that combines the content of one image with the artistic style of another. This project implements a state-of-the-art NST model using TensorFlow and Keras, allowing you to create unique artworks from your photos.

## 🎯 Objectives

- Explore and implement Neural Style Transfer techniques
- Develop a user-friendly interface for easy art creation
- Provide a platform for creating potential NFT artworks

## 🧠 How It Works

NST leverages the power of Convolutional Neural Networks (CNNs) to separate and recombine the content and style of different images. The process involves:

1. Using a pre-trained feature extractor (typically a VGG network)
2. Implementing a transfer network with an encoder-decoder architecture
3. Optimizing the output image to minimize both content and style losses

Our implementation uses a pre-trained "Arbitrary Neural Artistic Stylization Network," capable of applying various artistic styles to any input image in a single, efficient pass.

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- TensorFlow 2.x
- Keras
- Matplotlib

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/neural-style-transfer.git
   cd neural-style-transfer
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Download the pre-trained model from [this link](https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2) and place it in the `model` directory.

### Usage

You can use the Neural Style Transfer model in two ways:

1. Through the Python API:

```python
import matplotlib.pyplot as plt
from API import transfer_style

model_path = "path/to/model/directory"
content_image_path = "path/to/your/content/image.jpg"
style_image_path = "path/to/your/style/image.jpg"

stylized_image = transfer_style(content_image_path, style_image_path, model_path)
plt.imsave('stylized_image.jpg', stylized_image)
plt.imshow(stylized_image)
plt.show()
```

2. Through the provided application:

```
python app.py
```


## 📚 Learn More

To dive deeper into Neural Style Transfer, check out these resources:

- [A Neural Algorithm of Artistic Style (original paper)](https://arxiv.org/abs/1508.06576)
- [Neural Style Transfer with Keras](https://keras.io/examples/generative/neural_style_transfer/)
- [Exploring the structure of a real-time, arbitrary neural artistic stylization network](https://arxiv.org/abs/1705.06830)

## 🎨 Custom Models

The project includes two custom Neural Style Transfer (NST) models, located in the `notebooks` directory:

1. **Full NST Model (VGG19)**: This model implements the original Neural Style Transfer algorithm. It uses VGG19 to the style from a given style image and applies it to a content image. This process can be computationally intensive but offers high flexibility in style application.

2. **Pretrained Model**: This is a fast Neural Style Transfer model that uses a pretrained network. It can apply style transfer much more quickly than the Pull NST model, making it suitable for real-time applications or processing large numbers of images.

## 🖼️ Gallery

Here are some examples of our Neural Style Transfer in action:
### Original Image
<img src="Imgs/Lion.jpg" alt="OG" width="500"/>

### Generated Artworks
<table>
  <tr>
    <td><img src="Imgs/Lion1.jpeg" alt="Generated Art 1" width="700"/></td>
    <td><img src="Imgs/Lion2.jpeg" alt="Generated Art 2" width="700"/></td>
  </tr>
  <tr>
    <td><img src="Imgs/Lion3.jpeg" alt="Generated Art 3" width="700"/></td>
    <td><img src="Imgs/Lion4.jpeg" alt="Generated Art 4" width="700"/></td>
  </tr>
</table>

### Original Image
<img src="Imgs/stevejobs.jpg" alt="OG" width="500"/>

### Generated Artworks
<table>
  <tr>
    <td><img src="Imgs/jobs2.jpeg" alt="Generated Art 1" width="500"/></td>
    <td><img src="Imgs/jobs3.jpeg" alt="Generated Art 2" width="500"/></td>
  </tr>
  <tr>
    <td><img src="Imgs/jobs4.jpeg" alt="Generated Art 3" width="500"/></td>
    <td><img src="Imgs/jobs5.jpeg" alt="Generated Art 4" width="500"/></td>
  </tr>
</table>

## MISC 🎨
<table>
  <tr>
    <td><img src="Imgs/Elon Musk.jpg" alt="Generated Art 1" width="500"/></td>
    <td><img src="Imgs/Elon1.jpeg" alt="Generated Art 2" width="500"/></td>
  </tr>
</table>
<table>
  <tr>
    <td><img src="Imgs/trump.jpg" alt="Generated Art 1" width="500"/></td>
    <td><img src="Imgs/trump1.jpeg" alt="Generated Art 2" width="500"/></td>
  </tr>
  <tr>
    <td><img src="Imgs/trump2.jpeg" alt="Generated Art 3" width="500"/></td>
    <td><img src="Imgs/trump3.jpeg" alt="Generated Art 4" width="500"/></td>
  </tr>
</table>
<table>
  <tr>
    <td><img src="Imgs/arnold.jpg" alt="Generated Art 1" width="500"/></td>
    <td><img src="Imgs/arnold1.jpeg" alt="Generated Art 2" width="500"/></td>
    <td><img src="Imgs/arnold2.jpeg" alt="Generated Art 2" width="500"/></td>     
  </tr>
</table>
<table>
  <tr>
    <td><img src="Imgs/military.jpg" alt="Generated Art 1" width="500"/></td>
    <td><img src="Imgs/ms10.jpeg" alt="Generated Art 2" width="500"/></td>
  </tr>
</table>
<table>
  <tr>
    <td><img src="Imgs/Woman.jpg" alt="Generated Art 1" width="500"/></td>
    <td><img src="Imgs/Woman.jpeg" alt="Generated Art 2" width="500"/></td>
  </tr>
</table>

Each of these images demonstrates a unique style transfer, showcasing the versatility of our Neural Style Transfer model.

## Acknowledgements

- [TensorFlow Hub](https://tfhub.dev/) for the pre-trained model
- The authors of the original NST papers and implementations
- [Aleksa Gordić](https://github.com/gordicaleksa/pytorch-neural-style-transfer?tab=readme-ov-file) Pytorch Implementation

---

Happy styling! Create, innovate, and share your AI-generated masterpieces with the world! 🎨🚀
