[
    {
        "id": "43c9e808.0de2c8",
        "type": "tab",
        "label": "流程6",
        "disabled": false,
        "info": ""
    },
    {
        "id": "2005d7c9.c63288",
        "type": "http in",
        "z": "43c9e808.0de2c8",
        "name": "",
        "url": "/pin4",
        "method": "get",
        "upload": false,
        "swaggerDoc": "",
        "x": 130,
        "y": 180,
        "wires": [
            [
                "7f39bafb.11beb4"
            ]
        ]
    },
    {
        "id": "9a81f41b.9b2fe8",
        "type": "rpi-gpio in",
        "z": "43c9e808.0de2c8",
        "name": "GPIO4",
        "pin": "7",
        "intype": "up",
        "debounce": "25",
        "read": true,
        "x": 120,
        "y": 260,
        "wires": [
            [
                "7ee3f3cc.d5c38c"
            ]
        ]
    },
    {
        "id": "7ee3f3cc.d5c38c",
        "type": "function",
        "z": "43c9e808.0de2c8",
        "name": "Set GPIO",
        "func": "global.set(\"GPIO\",msg.payload)\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 330,
        "y": 220,
        "wires": [
            [
                "270ef699.5371fa"
            ]
        ]
    },
    {
        "id": "7f39bafb.11beb4",
        "type": "function",
        "z": "43c9e808.0de2c8",
        "name": "Get PGIO",
        "func": "msg.payload=global.get(\"GPIO\");\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 330,
        "y": 180,
        "wires": [
            [
                "270ef699.5371fa",
                "d92435be.f20f48"
            ]
        ]
    },
    {
        "id": "d92435be.f20f48",
        "type": "http response",
        "z": "43c9e808.0de2c8",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 500,
        "y": 160,
        "wires": []
    },
    {
        "id": "270ef699.5371fa",
        "type": "debug",
        "z": "43c9e808.0de2c8",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "x": 500,
        "y": 240,
        "wires": []
    }
]
