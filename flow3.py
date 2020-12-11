[
    {
        "id": "3f8d77ed.171838",
        "type": "tab",
        "label": "流程5",
        "disabled": false,
        "info": ""
    },
    {
        "id": "d06a5ce2.9d044",
        "type": "inject",
        "z": "3f8d77ed.171838",
        "name": "",
        "topic": "",
        "payload": "",
        "payloadType": "date",
        "repeat": "5",
        "crontab": "",
        "once": false,
        "onceDelay": 0.1,
        "x": 130,
        "y": 140,
        "wires": [
            [
                "7f8a6feb.f6e7b"
            ]
        ]
    },
    {
        "id": "7f8a6feb.f6e7b",
        "type": "function",
        "z": "3f8d77ed.171838",
        "name": "Payload",
        "func": "msg.headers={\n    deviceKey:\"mOpOw6h900RoaDyb\"\n    };\nmsg.payload=\"Temperature,,25.5\";\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 330,
        "y": 140,
        "wires": [
            [
                "3c7289fb.7bd066"
            ]
        ]
    },
    {
        "id": "3c7289fb.7bd066",
        "type": "http request",
        "z": "3f8d77ed.171838",
        "name": "",
        "method": "POST",
        "ret": "txt",
        "paytoqs": false,
        "url": "https://api.mediatek.com/mcs/v2/devices/DxUpYwYV/datapoints.csv",
        "tls": "",
        "persist": false,
        "proxy": "",
        "authType": "",
        "x": 500,
        "y": 140,
        "wires": [
            [
                "ba809e63.8f325",
                "2b935363.d8003c"
            ]
        ]
    },
    {
        "id": "ba809e63.8f325",
        "type": "http response",
        "z": "3f8d77ed.171838",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 700,
        "y": 120,
        "wires": []
    },
    {
        "id": "2b935363.d8003c",
        "type": "debug",
        "z": "3f8d77ed.171838",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "x": 680,
        "y": 200,
        "wires": []
    }
]
