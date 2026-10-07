# 21. Monitoreo de infraestructura y seguridad | Wazuh, Zabbix y Grafana

[Índice ES](../../README.es.md) · [Index EN](../../README.md)

## Caso profesional

**Estado:** Implementado, según el caso publicado.

Plataforma de monitoreo con Wazuh, Zabbix y Grafana, con alertas para apoyar la atención de incidencias.

**Tecnologías del caso:** Wazuh · Zabbix · Grafana · Linux · Monitoring.

[Fuente pública](https://www.linkedin.com/in/kristiangutierrez/details/projects/) · Proyecto de LinkedIn `428544943`. El título de esta ficha permite localizar el caso en el perfil.

## Demostración con datos ficticios

Correlaciona capacidad, disponibilidad y severidad de eventos para producir una lista de alertas ficticias.

```text
Host metrics + event severity → thresholds → prioritized alert list
```

```sh
# Desde cloud-security-automation; Python 3.11+, biblioteca estándar.
python3 demo.py monitoring
python3 demo.py monitoring --output generated/monitoring.json
```

[Datos de entrada](input.json) · [Salida de muestra](output.example.json) · [Implementación: `monitoring`](../../lab/operations.py) · [Pruebas](../../tests/test_catalog.py)

**Límite del ejemplo:** No configura agentes, consultas de Grafana ni alertas reales. Los umbrales son ejemplos.

Los datos se crearon desde cero para este portafolio. El código es una reconstrucción demostrativa preparada con asistencia de IA a partir de la descripción del caso. Los resultados sintéticos no acreditan métricas de producción ni amplían el estado del proyecto profesional.

## English

**Infrastructure and security monitoring** — Implemented, as described in the published case.

Monitoring with Wazuh, Zabbix and Grafana, with alerts supporting incident handling.

**Demonstration:** Combines capacity, availability and event severity into a synthetic alert list.

**Boundary:** No agents, Grafana queries or actual alert delivery. Thresholds are illustrative.

Run the commands above from the package directory. The fixture and output are synthetic; the code is an AI-assisted illustrative reconstruction, not production evidence. See the [data policy](../../docs/data-policy.md).
