# 04. Migración de oficinas de Guadalupe a Sabana – Infraestructura completa en 15 días

[Índice ES](../../README.es.md) · [Index EN](../../README.md)

## Caso profesional

**Estado:** Implementado, según el caso publicado.

Traslado documentado de servidores, red, telefonía y equipos en 15 días, con coordinación de proveedores y validación de servicios.

**Tecnologías del caso:** Windows Server · LAN/WAN · PBX · Project coordination.

[Fuente pública](https://www.linkedin.com/in/kristiangutierrez/details/projects/) · Proyecto de LinkedIn `716975847`. El título de esta ficha permite localizar el caso en el perfil.

## Demostración con datos ficticios

Calcula un calendario por dependencias y detecta ciclos o referencias a tareas inexistentes.

```text
Tasks → dependencies → critical path → target check
```

```sh
# Desde cloud-security-automation; Python 3.11+, biblioteca estándar.
python3 demo.py relocation
python3 demo.py relocation --output generated/relocation.json
```

[Datos de entrada](input.json) · [Salida de muestra](output.example.json) · [Implementación: `relocation`](../../lab/operations.py) · [Pruebas](../../tests/test_catalog.py)

**Límite del ejemplo:** Es un plan ficticio de ruta crítica; no modela personal, costos ni disponibilidad de proveedores. El plazo calculado no demuestra el resultado real.

Los datos se crearon desde cero para este portafolio. El código es una reconstrucción demostrativa preparada con asistencia de IA a partir de la descripción del caso. Los resultados sintéticos no acreditan métricas de producción ni amplían el estado del proyecto profesional.

## English

**Office infrastructure relocation** — Implemented, as described in the published case.

Documented 15-day relocation of servers, networking, telephony and workstations, including suppliers and service validation.

**Demonstration:** Computes a dependency schedule and detects cycles or missing tasks.

**Boundary:** Synthetic critical-path planning; staffing, costs and supplier availability are not modeled. Calculated duration is not evidence of the real outcome.

Run the commands above from the package directory. The fixture and output are synthetic; the code is an AI-assisted illustrative reconstruction, not production evidence. See the [data policy](../../docs/data-policy.md).
