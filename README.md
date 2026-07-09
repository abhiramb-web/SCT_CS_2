# Image Encryption Tool using Python

This project is an Image Encryption Tool developed in Python as part of Task 2 of the SkillCraft Technology Cyber Security Internship.

The application encrypts and decrypts images using an XOR-based encryption algorithm. It changes the RGB values of every pixel using a fixed key, making the image unreadable. Using the same key, the encrypted image can be converted back to its original form.

The project also includes a graphical user interface built with Tkinter so that users can easily encrypt and decrypt images without using the terminal.

## Features

- Browse an image from the computer
- Encrypt the selected image
- Decrypt an encrypted image
- Save the encrypted image
- Save the decrypted image
- Simple graphical user interface
- Error handling for invalid operations

## Technologies Used

- Python
- Tkinter
- Pillow (PIL)
- Git
- GitHub

## Project Structure

```
SCT_CS_2
│── gui.py
│── README.md
│── LICENSE
│── requirements.txt
│── .gitignore
└── Screenshots
    ├── image1.png
    ├── image2.png
    └── image3.png
```

## How to Run

Clone the repository.

```bash
git clone https://github.com/abhiramb-web/SCT_CS_2.git
```

Open the project folder.

```bash
cd SCT_CS_2
```

Install the required library.

```bash
pip install -r requirements.txt
```

Run the application.

```bash
python gui.py
```

## How the Project Works

The user first selects an image from the computer.

When the Encrypt button is clicked, the program reads all the RGB pixel values and generates a deterministic key stream using a fixed key. Each RGB value is encrypted using the XOR operation. The encrypted image can then be saved to the computer.
To decrypt the image, the user selects the encrypted image and clicks the Decrypt button. The program generates the same key stream and applies the XOR operation again. Since XOR is a reversible operation, the original image is restored.

## Screenshots

### Output Image

![Original](Screenshots/image1.png)

### Encrypted Image

![Encrypted](Screenshots/image3.png)

### Decrypted Image

![Decrypted](Screenshots/image2.png)

## What I Learned

Through this project, I learned:

- Image processing using Pillow
- Pixel manipulation in Python
- XOR encryption
- Working with RGB values
- Building graphical user interfaces using Tkinter
- File handling
- Exception handling
- Using Git and GitHub for version control

## Future Improvements

In the future, this project can be improved by adding:

- Password-based encryption
- Image preview inside the application
- Drag and drop support
- Support for encrypting multiple images
- Better encryption algorithms such as AES

## Author

B Abhiram

Cyber Security Intern

SkillCraft Technology

GitHub: https://github.com/abhiramb-web

LinkedIn: https://www.linkedin.com/in/b-abhiram-08233341b

## License

This project is licensed under the MIT License.

## Acknowledgement

This project was developed as part of the SkillCraft Technology Cyber Security Internship Program.
