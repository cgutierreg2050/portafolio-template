# 25. Reportes de seguridad automatizados | Wazuh, Python y Microsoft Graph

[Índice ES](../../README.es.md) · [Index EN](../../README.md)

## Caso profesional

**Estado:** Implementado, según el caso publicado.

Flujo semanal con Python/Bash, CSV/PDF, SharePoint, correo con Graph y cron.

**Tecnologías del caso:** Wazuh · Python · Bash · cron · Graph · SharePoint.

[Fuente pública](https://www.linkedin.com/in/kristiangutierrez/details/projects/) · Proyecto de LinkedIn `171979811`. El título de esta ficha permite localizar el caso en el perfil.

## Demostración con datos ficticios

Deduplica eventos por agente e identificador, filtra un intervalo UTC y resume severidad. El ejemplo original genera CSV/HTML.

```text
Events → identity deduplication → UTC window → severity summary
```

```sh
# Desde cloud-security-automation; Python 3.11+, biblioteca estándar.
python3 demo.py wazuh-reporting
python3 demo.py wazuh-reporting --output generated/wazuh-reporting.json
```

[Datos de entrada](input.json) · [Salida de muestra](output.example.json) · [Implementación: `weekly_report`](../../lab/operations.py) · [Pruebas](../../tests/test_catalog.py)

Exportación CSV/HTML: [report.py](../../examples/wazuh-report/report.py).

**Límite del ejemplo:** No consulta Wazuh, genera PDF ni publica en SharePoint o correo. Los niveles y eventos son datos de muestra.

Los datos se crearon desde cero para este portafolio. El código es una reconstrucción demostrativa preparada con asistencia de IA a partir de la descripción del caso. Los resultados sintéticos no acreditan métricas de producción ni amplían el estado del proyecto profesional.

## English

**Weekly Wazuh security reporting** — Implemented, as described in the published case.

Weekly Python/Bash workflow producing CSV/PDF, publishing to SharePoint and emailing through Graph with cron.

**Demonstration:** Deduplicates events by agent and ID, filters a UTC window and summarizes severity. The original example generates CSV/HTML.

**Boundary:** No live Wazuh, PDF generation, SharePoint publishing or email. Event levels and records are synthetic.

Run the commands above from the package directory. The fixture and output are synthetic; the code is an AI-assisted illustrative reconstruction, not production evidence. See the [data policy](../../docs/data-policy.md).
