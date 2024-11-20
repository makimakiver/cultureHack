import 'package:flutter/material.dart';
import 'package:flutter_earth_globe/flutter_earth_globe.dart';
import 'package:flutter_earth_globe/flutter_earth_globe_controller.dart';
import 'package:flutter_earth_globe/globe_coordinates.dart';



class Globe extends StatelessWidget {
late FlutterEarthGlobeController _controller;

@override
initState() {
  _controller = FlutterEarthGlobeController(
      rotationSpeed: 0.05,
      isBackgroundFollowingSphereRotation: true,
    background: AssetImage("assets/night.jpg"),
      surface: NetworkImage("assets/world_map.gif")
  );
}

@override
Widget build(BuildContext context) {
  initState();
  return MaterialApp(
    home: Scaffold(
      appBar: AppBar(
        title: Text('Flutter Global Earth'),
      ),
      body: SafeArea(
          child: FlutterEarthGlobe(
            controller: _controller,
            radius: 120,
          )
      ),
    ),
  );
}
}