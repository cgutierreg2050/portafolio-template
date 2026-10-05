# Kristian Gutierrez | Infraestructura y automatización de seguridad

Infraestructura Microsoft, Azure, Microsoft 365, PowerShell, Python y APIs.

[LinkedIn](https://www.linkedin.com/in/kristiangutierrez/) · [English](README.md)

## Casos reales documentados

- Gobierno de Microsoft 365: inventario de más de 600 sitios de SharePoint, revisión de propietarios y validación de accesos.
- Migración a Azure Key Vault: 187 secretos migrados, 0 errores y 0 elementos omitidos.
- Vulnerabilidades y parcheo: piloto con un grupo de equipos; detección, Action1, validación y evidencia.
- Reportes semanales de seguridad: Wazuh, Python, CSV/PDF, SharePoint y Microsoft Graph.
- Automatización de consultas: escalamiento de 1 a 13 contenedores Docker con Selenium sobre Linux.

## Ejemplos ejecutables

Los ejemplos se prepararon para este portafolio con datos ficticios. Son demostraciones independientes,
no una copia del código de producción de una empresa. Los resultados de los ejemplos no representan
las métricas de los proyectos profesionales.

1. `examples/wazuh-report`: genera resúmenes CSV y HTML a partir de eventos sintéticos; deduplica y filtra por fecha.
2. `examples/key-vault-plan`: planifica nombres de secretos a partir de metadatos ficticios y detecta colisiones. No lee contraseñas ni llama a Azure.
3. `examples/docker-selenium`: ejecuta una comprobación sobre una página local ficticia, con workers escalables en Docker Compose.

Las instrucciones de ejecución están en [README.md](README.md). Consultá también el [procedimiento de operación](docs/runbook.md)
y el [registro de validación](docs/validation.md).

## Material visual

- [Gobierno de SharePoint](docs/ficha-sharepoint.pdf)
- [Migración a Key Vault](docs/ficha-key-vault.pdf)
- [Piloto de vulnerabilidades](docs/ficha-vulnerabilidades.pdf)
- [Portafolio técnico en inglés](docs/portfolio-kristian-gutierrez.pdf)

Foco profesional: Senior Systems Engineer, Cloud Infrastructure Engineer y Security Automation Engineer.
