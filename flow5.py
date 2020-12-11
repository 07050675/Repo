[
    {
        "id": "12137faf.d65b7",
        "type": "tab",
        "label": "流程7",
        "disabled": false,
        "info": ""
    },
    {
        "id": "81a4a272.6f817",
        "type": "http in",
        "z": "12137faf.d65b7",
        "name": "Set GPIO5",
        "url": "/setgpio5",
        "method": "get",
        "upload": false,
        "swaggerDoc": "",
        "x": 140,
        "y": 220,
        "wires": [
            [
                "8b44e0a.cca212",
                "817e536d.8d5a2"
            ]
        ]
    },
    {
        "id": "8b44e0a.cca212",
        "type": "function",
        "z": "12137faf.d65b7",
        "name": "Set to 1",
        "func": "msg.payload = 1\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 350,
        "y": 220,
        "wires": [
            [
                "f67ce5b.3447418"
            ]
        ]
    },
    {
        "id": "f67ce5b.3447418",
        "type": "rpi-gpio out",
        "z": "12137faf.d65b7",
        "name": "",
        "pin": "29",
        "set": "",
        "level": "0",
        "freq": "",
        "out": "out",
        "x": 380,
        "y": 380,
        "wires": []
    },
    {
        "id": "817e536d.8d5a2",
        "type": "function",
        "z": "12137faf.d65b7",
        "name": "Return Status",
        "func": "msg.payload=\"GPIO5 set to HIGH\";\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 340,
        "y": 300,
        "wires": [
            [
                "ea8d819c.f1afa",
                "c07fe059.070f3"
            ]
        ]
    },
    {
        "id": "c07fe059.070f3",
        "type": "debug",
        "z": "12137faf.d65b7",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "x": 570,
        "y": 420,
        "wires": []
    },
    {
        "id": "ea8d819c.f1afa",
        "type": "http response",
        "z": "12137faf.d65b7",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 570,
        "y": 300,
        "wires": []
    },
    {
        "id": "8930e01e.6d043",
        "type": "http in",
        "z": "12137faf.d65b7",
        "name": "Clear GPIO5",
        "url": "/clear5",
        "method": "get",
        "upload": false,
        "swaggerDoc": "",
        "x": 160,
        "y": 440,
        "wires": [
            [
                "b9fd4ce0.49965",
                "81a251b2.53764"
            ]
        ]
    },
    {
        "id": "b9fd4ce0.49965",
        "type": "function",
        "z": "12137faf.d65b7",
        "name": "Clear to 0",
        "func": "msg.payload=0;\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 330,
        "y": 460,
        "wires": [
            [
                "f67ce5b.3447418"
            ]
        ]
    },
    {
        "id": "81a251b2.53764",
        "type": "function",
        "z": "12137faf.d65b7",
        "name": "Return Status",
        "func": "msg.payload=\"GPIO5 set to LOW\";\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 310,
        "y": 560,
        "wires": [
            [
                "ea8d819c.f1afa",
                "c07fe059.070f3"
            ]
        ]
    }
]
