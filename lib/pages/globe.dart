import 'package:flutter/material.dart';
import 'package:flutter_earth_globe/flutter_earth_globe.dart';
import 'package:flutter_earth_globe/flutter_earth_globe_controller.dart';
import 'package:flutter_earth_globe/globe_coordinates.dart';

class Globe extends StatefulWidget {

  Globe({super.key});

  @override
  State<Globe> createState() => _GlobeState();
}

class _GlobeState extends State<Globe> {
  late FlutterEarthGlobeController controller;

  GlobeCoordinates? coordinates;

  @override
  void initState(){

    controller = FlutterEarthGlobeController(
      rotationSpeed: 0.05,
      isBackgroundFollowingSphereRotation: true,
      background: Image.asset('assets/2k_stars.jpg').image,
      surface: Image.asset('assets/2k_earth-day,jpg').image,
    );

    controller.addListener((){
      setState(() {
        // make the listener add the coodinates
      });
    } as VoidCallback);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('globe'),
      ),
      body: SafeArea(
        child: Column(
          children: [
            Expanded(
              child: FlutterEarthGlobe(radius: 120, controller: controller),
            ),
          ],
        ),
      )
    );
  }
}
