# 20. Modernización de Active Directory e identidad híbrida

[Índice ES](../../README.es.md) · [Index EN](../../README.md)

## Caso profesional

**Estado:** AD implementado; Windows Server 2025 en planificación.

Mejoras en controladores, replicación, FSMO, DNS, identidad híbrida y revisión de seguridad. Migración a Windows Server 2025 planificada.

**Tecnologías del caso:** Active Directory · Windows Server · DNS · Entra ID · Hybrid identity.

[Fuente pública](https://www.linkedin.com/in/kristiangutierrez/details/projects/) · Proyecto de LinkedIn `348320372`. El título de esta ficha permite localizar el caso en el perfil.

## Demostración con datos ficticios

Valida metadatos de replicación, DNS, sincronización horaria, propietarios FSMO y prueba de recuperación.

```text
Domain snapshot → health/FSMO checks → precheck report → planning
```

```sh
# Desde cloud-security-automation; Python 3.11+, biblioteca estándar.
python3 demo.py active-directory
python3 demo.py active-directory --output generated/active-directory.json
```

[Datos de entrada](input.json) · [Salida de muestra](output.example.json) · [Implementación: `ad_readiness`](../../lab/security.py) · [Pruebas](../../tests/test_catalog.py)

**Límite del ejemplo:** No consulta el dominio ni transfiere roles. Un reporte sin hallazgos no autoriza ni demuestra una migración.

Los datos se crearon desde cero para este portafolio. El código es una reconstrucción demostrativa preparada con asistencia de IA a partir de la descripción del caso. Los resultados sintéticos no acreditan métricas de producción ni amplían el estado del proyecto profesional.

## English

**Active Directory and hybrid identity modernization** — AD improvements implemented; Windows Server 2025 planning.

Domain-controller, replication, FSMO, DNS, hybrid identity and security improvements. Windows Server 2025 migration remains planned.

**Demonstration:** Checks supplied replication, DNS, time synchronization, FSMO ownership and recovery-test metadata.

**Boundary:** Does not query a domain or transfer roles. A clear report does not authorize or prove a migration.

Run the commands above from the package directory. The fixture and output are synthetic; the code is an AI-assisted illustrative reconstruction, not production evidence. See the [data policy](../../docs/data-policy.md).
