from django.db import models

class Psicologa(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField(null=True, verbose_name="fecha de nacimiento")
    telefono = models.PositiveIntegerField(unique=True)
    correo = models.CharField(max_length=200)
    usuario = models.CharField(max_length=200)
    contraseña = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return f"🌸Psicologa {self.nombre} - 👥{self.usuario} - 📱{self.telefono} - 📧{self.correo}" 

class Equipo(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField(null=True, verbose_name="fecha de nacimiento")
    telefono = models.PositiveIntegerField(unique=True)
    correo = models.CharField(max_length=200)
    area = models.CharField(max_length=200)
    usuario = models.CharField(max_length=200)
    contraseña = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return f"{self.nombre} - area: {self.area} 😎  - 👥{self.usuario} - 📱{self.telefono} - 📧{self.correo}"
    
class Usuario(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField(null=True, verbose_name="fecha de nacimiento")
    telefono = models.PositiveIntegerField(unique=True)
    correo = models.CharField(max_length=200)
    usuario = models.CharField(max_length=200)
    contraseña = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return f"🙋‍♀️ {self.usuario} 🟣 {self.nombre} - 📱{self.telefono} - 📧{self.correo}"

class Comunidad(models.Model):
    nombre = models.CharField(max_length=200)
    psicologa = models.ForeignKey(Psicologa, on_delete=models.SET_NULL, null=True, blank=True, related_name='psicologas')
    usuario = models.ManyToManyField(Usuario)
    
    def __str__(self) -> str:
        return self.nombre