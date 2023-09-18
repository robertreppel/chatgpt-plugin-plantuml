// Project: chatgpt-plugin-plantuml

import http from "k6/http";
import { check } from "k6";

export default function() {
    const url = "https://chatgpt-plugin-plantuml.webeventstorming.com/generate-diagram";
    const headers = {
        "Content-Type": "application/json"
    };
    const payload = JSON.stringify({
        umlCode: "@startuml\nstart\n:Initialize;\n:Process Data;\nif (Is Valid?) then (yes)\n  :Continue Processing;\nelse (no)\n  :Stop;\nendif\n:Finalize;\nstop\n@enduml"
    });

    const response = http.post(url, payload, { headers: headers });

    // Check if the response status is 200 (OK)
    check(response, {
        "is status 200": (r) => r.status === 200
    });
}

