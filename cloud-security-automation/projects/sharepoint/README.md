# 12. Gobierno de Microsoft 365 | Más de 600 sitios de SharePoint

[Índice ES](../../README.es.md) · [Index EN](../../README.md)

## Caso profesional

**Estado:** Inventario implementado; cambios en piloto.

Inventario de más de 600 sitios. Pruebas controladas de propietarios y accesos, con respaldos, validación y trazabilidad.

**Tecnologías del caso:** SharePoint · Microsoft Graph · PnP PowerShell · Entra ID.

[Fuente pública](https://www.linkedin.com/feed/update/urn:li:activity:7489746347470934016/) · Proyecto de LinkedIn `171924253`. El título de esta ficha permite localizar el caso en el perfil.

## Demostración con datos ficticios

Propone agregar un propietario activo solo en sitios piloto con respaldo verificado; conserva los propietarios existentes.

```text
Site inventory → pilot scope → owner/backup checks → additive proposal
```

```sh
# Desde cloud-security-automation; Python 3.11+, biblioteca estándar.
python3 demo.py sharepoint
python3 demo.py sharepoint --output generated/sharepoint.json
```

[Datos de entrada](input.json) · [Salida de muestra](output.example.json) · [Implementación: `sharepoint_owners`](../../lab/cloud.py) · [Pruebas](../../tests/test_catalog.py)

**Límite del ejemplo:** No aplica cambios ni demuestra que los 600 sitios se modificaron. Las tres entradas son ficticias.

Los datos se crearon desde cero para este portafolio. El código es una reconstrucción demostrativa preparada con asistencia de IA a partir de la descripción del caso. Los resultados sintéticos no acreditan métricas de producción ni amplían el estado del proyecto profesional.

## English

**Microsoft 365 and SharePoint governance** — Inventory implemented; changes piloted.

Inventory of 600+ sites. Controlled ownership/access pilot with backups, validation and traceability.

**Demonstration:** Proposes adding an active owner only to pilot sites with verified backups; preserves current owners.

**Boundary:** No changes are applied and no claim is made that all 600 sites were modified. Three entries are synthetic.

Run the commands above from the package directory. The fixture and output are synthetic; the code is an AI-assisted illustrative reconstruction, not production evidence. See the [data policy](../../docs/data-policy.md).
