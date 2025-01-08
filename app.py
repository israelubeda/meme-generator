from flask import Flask, render_template, request, send_file
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    image_file = request.files['image']
    top_text = request.form['top_text']
    bottom_text = request.form['bottom_text']

    image = Image.open(image_file)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("static/fonts/Roboto-Regular.ttf", 40)

    # Calcular posición del texto superior
    image_width, image_height = image.size
    top_bbox = font.getbbox(top_text)
    text_width, text_height = top_bbox[2] - top_bbox[0], top_bbox[3] - top_bbox[1]
    draw.text(((image_width - text_width) / 2, 10), top_text, font=font, fill="white", stroke_width=2, stroke_fill="black")

    # Calcular posición del texto inferior
    bottom_bbox = font.getbbox(bottom_text)
    text_width, text_height = bottom_bbox[2] - bottom_bbox[0], bottom_bbox[3] - bottom_bbox[1]
    draw.text(((image_width - text_width) / 2, image_height - text_height - 10), bottom_text, font=font, fill="white", stroke_width=2, stroke_fill="black")

    # Guardar la imagen generada
    output = BytesIO()
    image.save(output, format="PNG")
    output.seek(0)
    return send_file(output, mimetype='image/png', as_attachment=True, download_name='meme.png')


if __name__ == '__main__':
    app.run(debug=True)
