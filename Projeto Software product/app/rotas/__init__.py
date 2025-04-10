from app.rotas import rotas_usuarios, rotas_jogos

app.register_blueprint(rotas_usuarios.usuarios_bp, url_prefix='/usuarios')
app.register_blueprint(rotas_jogos.jogos_bp, url_prefix='/jogos')
