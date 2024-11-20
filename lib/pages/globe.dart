import 'package:flutter/material.dart';
import 'package:flutter_earth_globe/flutter_earth_globe.dart';
import 'package:flutter_earth_globe/flutter_earth_globe_controller.dart';
import 'package:flutter_earth_globe/globe_coordinates.dart';
import 'package:flutter_earth_globe/point.dart';



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
  List<Point> points = [


    Point(
        id: '1',
        isLabelVisible: true,
        coordinates: const GlobeCoordinates(5.6895, 130.6917),
        style: const PointStyle(color: Colors.blue),

        onTap: (){
          double longitude = 5.6895;
          print(123);
        },
        label: 'Tokyo'),
    Point(
        id: '4',
        isLabelVisible: true,
        onTap: () {
          Future.delayed(Duration.zero, () {
            showDialog(
                context: context,
                builder: (context) => const AlertDialog(
                  title: Text('Center'),
                  content: Text('This is the center of the globe'),
                ));
          });
        },
        coordinates: const GlobeCoordinates(0, 0),
        style: const PointStyle(color: Colors.yellow),
        label: 'Center'),
  ];

  for (var point in points) {
    _controller.addPoint(point);
  }
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