import 'package:flutter/material.dart';
import 'api_service.dart';

class RegistroScreen extends StatefulWidget {
  @override
  _RegistroScreenState createState() => _RegistroScreenState();
}

class _RegistroScreenState extends State<RegistroScreen> {
  ApiService apiService = ApiService();
  final TextEditingController _usernameController = TextEditingController();
  final TextEditingController _emailController = TextEditingController();
  final TextEditingController _passwordController = TextEditingController();
  bool _obscureText = true;

  void registrar() async {
    try {
      await apiService.registrarUsuario(
        _usernameController.text,
        _emailController.text,
        _passwordController.text,
      );
      Navigator.pop(context); // Volver a la pantalla de inicio de sesión después del registro
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text("Usuario registrado correctamente. Por favor, inicia sesión.")),
      );
    } catch (e) {
      print("Error al registrar usuario: $e");
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text("Error al registrar usuario. Intente nuevamente.")),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Registrar Usuario'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            TextField(
              controller: _usernameController,
              decoration: InputDecoration(labelText: 'Nombre de Usuario'),
            ),
            TextField(
              controller: _emailController,
              decoration: InputDecoration(labelText: 'Correo Electrónico'),
            ),
            TextField(
              controller: _passwordController,
              decoration: InputDecoration(
                labelText: 'Contraseña',
                suffixIcon: IconButton(
                  icon: Icon(_obscureText ? Icons.visibility : Icons.visibility_off),
                  onPressed: () {
                    setState(() {
                      _obscureText = !_obscureText;
                    });
                  },
                ),
              ),
              obscureText: _obscureText,
            ),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: registrar,
              child: Text('Registrar'),
            ),
          ],
        ),
      ),
    );
  }
}
