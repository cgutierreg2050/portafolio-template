# 13. Gobierno y protección de datos con Microsoft Purview y DLP

[Índice ES](../../README.es.md) · [Index EN](../../README.md)

## Caso profesional

**Estado:** Implementado, según el caso publicado.

Controles de DLP, retención, sensibilidad, auditoría y eDiscovery en Microsoft 365, apoyados por PowerShell y Graph.

**Tecnologías del caso:** Microsoft Purview · DLP · Microsoft 365 · PowerShell · Graph.

[Fuente pública](https://www.linkedin.com/in/kristiangutierrez/details/projects/) · Proyecto de LinkedIn `348398228`. El título de esta ficha permite localizar el caso en el perfil.

## Demostración con datos ficticios

Detecta marcadores sintéticos, propone etiquetas y revisión de compartición externa, respetando retenciones legales.

```text
Synthetic documents → marker/label check → sharing proposal → hold preservation
```

```sh
# Desde cloud-security-automation; Python 3.11+, biblioteca estándar.
python3 demo.py purview-dlp
python3 demo.py purview-dlp --output generated/purview-dlp.json
```

[Datos de entrada](input.json) · [Salida de muestra](output.example.json) · [Implementación: `purview`](../../lab/security.py) · [Pruebas](../../tests/test_catalog.py)

**Límite del ejemplo:** El patrón DEMO-RECORD no identifica datos personales reales. No implementa Purview, reglas legales ni políticas de retención.

Los datos se crearon desde cero para este portafolio. El código es una reconstrucción demostrativa preparada con asistencia de IA a partir de la descripción del caso. Los resultados sintéticos no acreditan métricas de producción ni amplían el estado del proyecto profesional.

## English

**Microsoft Purview and DLP governance** — Implemented, as described in the published case.

DLP, retention, sensitivity, auditing and eDiscovery controls in Microsoft 365, supported by PowerShell and Graph.

**Demonstration:** Detects synthetic markers, proposes labels and external-sharing restrictions, and preserves legal holds.

**Boundary:** The DEMO-RECORD marker is not a real personal-data detector. No Purview or legal/retention policy is implemented.

Run the commands above from the package directory. The fixture and output are synthetic; the code is an AI-assisted illustrative reconstruction, not production evidence. See the [data policy](../../docs/data-policy.md).
