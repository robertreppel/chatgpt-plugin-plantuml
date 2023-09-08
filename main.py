
import os
import quart
import quart_cors
import logging
from quart import request, send_file
from quart import request
from delete_old_png_files import delete_old_png_files
from generate_diagram import generate_diagram

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('quart.app')
app = quart_cors.cors(quart.Quart(__name__), allow_origin="https://chat.openai.com")

@app.get("/")
async def root():
    return "OK", 200

from quart import url_for

@app.post("/generate-diagram")
async def post_generate_diagram():
    data = await request.json
    uml_code = data.get('umlCode')
    if not uml_code:
        return {"error": "umlCode is required"}, 400

    await delete_old_png_files('static/diagrams') # Get rid of diagrams older than 5 minutes each time the API is called. For data privacy and to save space.
    
    output_file = await generate_diagram(uml_code)
    file_name = os.path.basename(output_file)
    download_url = 'http://localhost:5003' + url_for('static', filename=f'diagrams/{file_name}')
    return {"download_url": download_url}

@app.route('/static/diagrams/<filename>')
async def serve_diagram(filename):
    return await send_file(f'static/diagrams/{filename}', mimetype='image/png')

@app.get("/logo.png")
async def plugin_logo():
    filename = 'logo.png'
    return await quart.send_file(filename, mimetype='image/png')

@app.get("/.well-known/ai-plugin.json")
async def plugin_manifest():
    host = request.headers['Host']
    with open("./.well-known/ai-plugin.json") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/json")

@app.get("/openapi.yaml")
async def openapi_spec():
    host = request.headers['Host']
    with open("openapi.yaml") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/yaml")    

def main():
    app.run(debug=True, host="0.0.0.0", port=5003)

if __name__ == "__main__":
    main()
