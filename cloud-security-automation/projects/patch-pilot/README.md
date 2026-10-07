# 22. Orquestación de vulnerabilidades y parcheo | Defender, Wazuh y Action1

[Índice ES](../../README.es.md) · [Index EN](../../README.md)

## Caso profesional

**Estado:** Piloto con algunos equipos.

Piloto Defender/Wazuh → correlación CVE/KB/equipo → Action1 → validación → evidencia, con alcance controlado.

**Tecnologías del caso:** Defender · Wazuh · Action1 · PowerShell · Graph · SharePoint.

[Fuente pública](https://www.linkedin.com/in/kristiangutierrez/details/projects/) · Proyecto de LinkedIn `172048204`. El título de esta ficha permite localizar el caso en el perfil.

## Demostración con datos ficticios

Deduplica hallazgos y determina elegibilidad, espera por reinicio o cierre con evidencia posterior.

```text
Findings → pilot scope → prechecks → proposed state → post-scan validation
```

```sh
# Desde cloud-security-automation; Python 3.11+, biblioteca estándar.
python3 demo.py patch-pilot
python3 demo.py patch-pilot --output generated/patch-pilot.json
```

[Datos de entrada](input.json) · [Salida de muestra](output.example.json) · [Implementación: `patch_pilot`](../../lab/security.py) · [Pruebas](../../tests/test_catalog.py)

**Límite del ejemplo:** No envía trabajos de Action1. CVE y KB son marcadores inventados y su relación no es información de vulnerabilidades reales.

Los datos se crearon desde cero para este portafolio. El código es una reconstrucción demostrativa preparada con asistencia de IA a partir de la descripción del caso. Los resultados sintéticos no acreditan métricas de producción ni amplían el estado del proyecto profesional.

## English

**Vulnerability and patch orchestration** — Pilot with selected endpoints.

Scoped Defender/Wazuh → CVE/KB/device correlation → Action1 → validation → evidence pilot.

**Demonstration:** Deduplicates findings and models eligibility, reboot deferral and evidence-gated closure.

**Boundary:** No Action1 jobs. CVE/KB markers and mappings are invented, not real vulnerability intelligence.

Run the commands above from the package directory. The fixture and output are synthetic; the code is an AI-assisted illustrative reconstruction, not production evidence. See the [data policy](../../docs/data-policy.md).
