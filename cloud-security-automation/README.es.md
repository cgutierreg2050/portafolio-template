# Kristian Gutierrez | 25 proyectos de infraestructura y automatización

[English](README.md) · [LinkedIn](https://www.linkedin.com/in/kristiangutierrez/) · [Web](https://www.kggdev.org/es.html)

Administración de infraestructura híbrida, identidad, seguridad y automatización con Azure, Microsoft 365, Windows Server, Linux, PowerShell, Python y APIs.

**25 casos profesionales documentados · 25 demostraciones locales · datos totalmente ficticios · documentación ES/EN.**

Cada ficha separa el trabajo profesional descrito en LinkedIn del ejemplo preparado para este repositorio. Las demostraciones fueron reconstruidas con asistencia de IA a partir de esas descripciones y usan datos creados desde cero. Los resultados de las pruebas corresponden al código de muestra; no acreditan resultados de producción.

## Empezar en un minuto

Python 3.11 o posterior. Las 25 demostraciones nuevas usan únicamente la biblioteca estándar y no necesitan cuentas, credenciales, contenedores ni conexión a servicios.

```sh
git clone --branch linkedin-portfolio --single-branch https://github.com/cgutierreg2050/portafolio-template.git
cd portafolio-template/cloud-security-automation
python3 demo.py sharepoint
python3 demo.py patch-pilot
python3 -m unittest discover -s tests -v
```

La carpeta de cada proyecto contiene `README.md`, `input.json` y `output.example.json`. El parámetro `--output generated/resultado.json` guarda la salida localmente.

## Los 25 proyectos

| # | Proyecto | Estado del caso profesional | Demostración incluida |
|---|---|---|---|
| 01 | [Seguridad de correo y diagnóstico de DMARC — Exchange Online](projects/dmarc/README.md) | Implementado, según el caso publicado | Evalúa alineación estricta de SPF y DKIM con el dominio From a partir de resultados ficticios. |
| 02 | [Migración automatizada a Azure Key Vault — 187 secretos](projects/key-vault/README.md) | Implementado, según el caso publicado | Normaliza nombres de entradas ficticias y rechaza colisiones o campos que puedan contener credenciales. |
| 03 | [Automatización de transcripción masiva con IA y control de GPU](projects/transcription/README.md) | Implementado, según el caso publicado | Organiza trabajos ficticios en lotes que respetan un presupuesto de memoria y separa trabajos demasiado grandes. |
| 04 | [Migración de oficinas de Guadalupe a Sabana – Infraestructura completa en 15 días](projects/relocation/README.md) | Implementado, según el caso publicado | Calcula un calendario por dependencias y detecta ciclos o referencias a tareas inexistentes. |
| 05 | [Automatización con Terraform + GitHub Actions](projects/terraform/README.md) | Implementado, según el caso publicado | Revisa un plan simplificado para identificar reemplazos, eliminaciones, exposición administrativa y etiquetas faltantes. |
| 06 | [Automatización de comunicaciones con Python y Microsoft Graph](projects/graph-mail/README.md) | Implementado, según el caso publicado | Construye borradores HTML escapados, elimina destinatarios repetidos y organiza lotes con claves de seguimiento. |
| 07 | [Automatización de consultas con Docker y Selenium — 13 workers](projects/docker-selenium/README.md) | Implementado, según el caso publicado | Distribuye trabajos ficticios por costo estimado entre varios workers. También se conserva el ejemplo Docker/Selenium sobre una página local. |
| 08 | [Ciclo de vida de datos en Microsoft 365 — Evaluación de archivado](projects/data-lifecycle/README.md) | Evaluación y diseño | Selecciona candidatos según fecha de actividad, retención y retenciones legales, separando exclusiones. |
| 09 | [Control de aplicaciones con AppLocker y WDAC](projects/applocker-wdac/README.md) | Implementado, según el caso publicado | Evalúa reglas ficticias por hash o editor, con prioridad de denegación y distinción entre auditoría y aplicación. |
| 10 | [Despliegue de VM en Azure + VPN Site-to-Site](projects/azure-vpn/README.md) | Implementado, según el caso publicado | Valida solapamiento de redes, pertenencia de la VM, rutas declaradas y reenvío DNS. |
| 11 | [Despliegue de n8n en Kubernetes + Cloudflare Tunnel](projects/n8n-kubernetes/README.md) | Implementado, según el caso publicado | Revisa persistencia, readiness, referencia de clave de cifrado, servicio interno, túnel y política de acceso. |
| 12 | [Gobierno de Microsoft 365 — Más de 600 sitios de SharePoint](projects/sharepoint/README.md) | Inventario implementado; cambios en piloto | Propone agregar un propietario activo solo en sitios piloto con respaldo verificado; conserva los propietarios existentes. |
| 13 | [Gobierno y protección de datos con Microsoft Purview y DLP](projects/purview-dlp/README.md) | Implementado, según el caso publicado | Detecta marcadores sintéticos, propone etiquetas y revisión de compartición externa, respetando retenciones legales. |
| 14 | [Hardening post-incidente en Microsoft 365](projects/m365-hardening/README.md) | Implementado, según el caso publicado | Genera hallazgos sobre administradores no aprobados, carencias de MFA y reenvíos externos no autorizados. |
| 15 | [Implementación de Azure Arc + VPN Site-to-Site](projects/azure-arc/README.md) | Implementado, según el caso publicado | Compara inventario y registros de agente para encontrar equipos ausentes, información desactualizada y fechas futuras. |
| 16 | [Infraestructura local para IA – RTX 3060, 128 GB RAM y Ryzen 9](projects/ai-lab/README.md) | Laboratorio implementado para pruebas | Estima el tamaño mínimo de pesos según parámetros y precisión, con una reserva configurable. |
| 17 | [Intercambio seguro de archivos — OpenPGP, SFTP y PowerShell](projects/openpgp/README.md) | Desarrollo y validación | Compara metadatos de subclave, contexto de ejecución, expiración y revocación. |
| 18 | [LexRAG Analytics — IA privada para consulta y análisis documental](projects/lexrag/README.md) | Indexación y validación | Busca términos en documentos ficticios autorizados y devuelve referencias a la fuente, o indica falta de evidencia. |
| 19 | [Migración de prueba y validación de inventario — GLPI y Defender](projects/glpi-defender/README.md) | Migración probada en entorno de prueba | Compara conjuntos de tablas y separa errores de inventario, carencias de protección y firmas antiguas. |
| 20 | [Modernización de Active Directory e identidad híbrida](projects/active-directory/README.md) | AD implementado; Windows Server 2025 en planificación | Valida metadatos de replicación, DNS, sincronización horaria, propietarios FSMO y prueba de recuperación. |
| 21 | [Monitoreo de infraestructura y seguridad — Wazuh, Zabbix y Grafana](projects/monitoring/README.md) | Implementado, según el caso publicado | Correlaciona capacidad, disponibilidad y severidad de eventos para producir una lista de alertas ficticias. |
| 22 | [Orquestación de vulnerabilidades y parcheo — Defender, Wazuh y Action1](projects/patch-pilot/README.md) | Piloto con algunos equipos | Deduplica hallazgos y determina elegibilidad, espera por reinicio o cierre con evidencia posterior. |
| 23 | [Publicación de sitios IIS con Cloudflare WAF + SSL](projects/iis-cloudflare/README.md) | Implementado, según el caso publicado | Revisa metadatos ficticios de TLS al origen, WAF, política de acceso, exposición directa y caducidad de certificado. |
| 24 | [Recuperación de VM Windows y diagnóstico por capas — KVM/QEMU](projects/kvm-recovery/README.md) | Arranque y acceso a consola recuperados | Inspecciona XML ficticio y propone revisar una ruta de disco solo si existe un candidato inequívoco. |
| 25 | [Reportes de seguridad automatizados — Wazuh, Python y Microsoft Graph](projects/wazuh-reporting/README.md) | Implementado, según el caso publicado | Deduplica eventos por agente e identificador, filtra un intervalo UTC y resume severidad. El ejemplo original genera CSV/HTML. |

## Qué se conserva de los primeros ejemplos

- [PowerShell: plan de nombres de Key Vault](examples/key-vault-plan/plan.ps1).
- [Python: exportación CSV/HTML de eventos](examples/wazuh-report/report.py).
- [Docker/Selenium: página local y workers independientes](examples/docker-selenium/compose.yaml).

PowerShell 7 es necesario para el planificador original. Docker es opcional y su validación se registra por separado. La simulación `demo.py docker-selenium` se ejecuta sin Docker.

## Código, datos y validación

```text
projects/<case>/input.json
        ↓
demo.py → lab/security.py | lab/cloud.py | lab/operations.py
        ↓
JSON result: synthetic=true, production_validation=false
```

- [Política de datos ficticios y límites](docs/data-policy.md)
- [Registro de validación](docs/validation.md)
- [Instrucciones de ejecución](docs/runbook.md)
- [Catálogo estructurado de los 25 casos](projects/catalog.json)
- [Pruebas de comportamiento](tests/test_catalog.py)

## Fichas PDF seleccionadas

[SharePoint](docs/ficha-sharepoint.pdf) · [Key Vault](docs/ficha-key-vault.pdf) · [Vulnerability pilot](docs/ficha-vulnerabilidades.pdf) · [Technical portfolio overview](docs/portfolio-kristian-gutierrez.pdf)

Los PDF conservados son una selección anterior de casos. El índice de arriba contiene el catálogo completo actualizado de 25 proyectos.
