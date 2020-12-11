[
    {
        "id": "bdf0dd72.26beb",
        "type": "tab",
        "label": "流程4",
        "disabled": false,
        "info": ""
    },
    {
        "id": "77ca3488.80b73c",
        "type": "inject",
        "z": "bdf0dd72.26beb",
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
                "9cde1252.5e328"
            ]
        ]
    },
    {
        "id": "9cde1252.5e328",
        "type": "function",
        "z": "bdf0dd72.26beb",
        "name": "Payload",
        "func": "msg.headers={\n    deviceKey:\"mOpOw6h900RoaDyb\"\n};\n\n\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 330,
        "y": 160,
        "wires": [
            [
                "4326a4fb.71a6bc"
            ]
        ]
    },
    {
        "id": "4326a4fb.71a6bc",
        "type": "http request",
        "z": "bdf0dd72.26beb",
        "name": "",
        "method": "GET",
        "ret": "txt",
        "paytoqs": false,
        "url": "http://api.mediatek.com/mcs/v2/devices/DxUpYwYV/datachannels/LEDControl/datapoints.csv",
        "tls": "",
        "persist": false,
        "proxy": "",
        "authType": "",
        "x": 500,
        "y": 160,
        "wires": [
            [
                "ceb8b5f3.a305d8",
                "4c98bf49.1ab28"
            ]
        ]
    },
    {
        "id": "ceb8b5f3.a305d8",
        "type": "http response",
        "z": "bdf0dd72.26beb",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 720,
        "y": 180,
        "wires": []
    },
    {
        "id": "4c98bf49.1ab28",
        "type": "debug",
        "z": "bdf0dd72.26beb",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "x": 680,
        "y": 260,
        "wires": []
    }
]
