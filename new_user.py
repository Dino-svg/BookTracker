 def register_user(name, email, password):
     if not name or not email or len(password) < 8:
         return "Error: Campos incompletos o password muy corta."

    existing_emails = ["admin@libroteca.com", "test@libroteca.com"]
    if email in existing_emails:
        return "Error: Este correo ya está registrado."
    new_user = {"name": name, "email": email, "password_hash": "hashed_value"}
    print(f"Usuario registrado exitosamente: {new_user}")
return "Success"

 print(register_user("Ana", "ana@mail.com", "12345678"))