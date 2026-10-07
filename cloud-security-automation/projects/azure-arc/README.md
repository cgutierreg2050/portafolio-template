# 15. Implementación de Azure Arc + VPN Site-to-Site

[Índice ES](../../README.es.md) · [Index EN](../../README.md)

## Caso profesional

**Estado:** Implementado, según el caso publicado.

Azure Arc para visibilidad y administración de máquinas locales, junto con VPN Fortinet hacia Azure.

**Tecnologías del caso:** Azure Arc · Fortinet · VPN · Windows/Linux.

[Fuente pública](https://www.linkedin.com/in/kristiangutierrez/details/projects/) · Proyecto de LinkedIn `433260702`. El título de esta ficha permite localizar el caso en el perfil.

## Demostración con datos ficticios

Compara inventario y registros de agente para encontrar equipos ausentes, información desactualizada y fechas futuras.

```text
Asset inventory + agent snapshots → ID reconciliation → freshness report
```

```sh
# Desde cloud-security-automation; Python 3.11+, biblioteca estándar.
python3 demo.py azure-arc
python3 demo.py azure-arc --output generated/azure-arc.json
```

[Datos de entrada](input.json) · [Salida de muestra](output.example.json) · [Implementación: `arc_inventory`](../../lab/cloud.py) · [Pruebas](../../tests/test_catalog.py)

**Límite del ejemplo:** No instala agentes, incorpora máquinas ni evalúa cumplimiento real de políticas.

Los datos se crearon desde cero para este portafolio. El código es una reconstrucción demostrativa preparada con asistencia de IA a partir de la descripción del caso. Los resultados sintéticos no acreditan métricas de producción ni amplían el estado del proyecto profesional.

## English

**Azure Arc and hybrid connectivity** — Implemented, as described in the published case.

Azure Arc visibility and management of on-premises machines with a Fortinet VPN to Azure.

**Demonstration:** Reconciles inventory and agent records to detect missing devices, stale data and future timestamps.

**Boundary:** No agent installation, machine enrollment or actual policy-compliance evaluation.

Run the commands above from the package directory. The fixture and output are synthetic; the code is an AI-assisted illustrative reconstruction, not production evidence. See the [data policy](../../docs/data-policy.md).
