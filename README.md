# PlantUML API. 

Generates .png files from [PlantUML](https://plantuml.com). 

POSTing PlantUML to the API returns a link to a statically hosted PNG file with the PlantUML diagram. 

OpenAPI spec: [openapi.yaml](openapi.yaml)

 ## HOWTO

### Run the API in a Docker container

```
 docker build -t chatgpt-plugin-plantuml .
 docker run -p 5003:5003 chatgpt-plugin-plantuml
 ```
This exposes the API on port 5003 on localhost. To use the plugin: Follow the instructions in the [OpenAI Plugin documentation](https://platform.openai.com/docs/plugins/getting-started/running-a-plugin).

 ### Run the API locally

 1. Ensure you have Python: ```python --version``` . Install it if necessary.
 2. Install Java. To check if you have it already: ```java --version``` Java is needed to generate .png images from PlantUML.
 3. Download the plantuml.jar: ```wget "https://sourceforge.net/projects/plantuml/files/plantuml.jar/download" -O plantuml.jar```
 4. Run ```python main.py```
 5. Follow the instructions in the [OpenAI Plugin documentation](https://platform.openai.com/docs/plugins/getting-started/running-a-plugin) on how to use a plugin running on localhost.

 ### Test the API

 ```
curl --location --request POST 'http://localhost:5003/generate-diagram' \
--header 'Content-Type: application/json' \
--data-raw '{
  "umlCode": "@startuml\nstart\n:Initialize;\n:Process Data;\nif (Is Valid?) then (yes)\n  :Continue Processing;\nelse (no)\n  :Stop;\nendif\n:Finalize;\nstop\n@enduml"
}'
```

To view the generated diagram: E.g. ```eog output.png``` or any other image viewer/editor.


