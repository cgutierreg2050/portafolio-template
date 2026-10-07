# 08. Ciclo de vida de datos en Microsoft 365 | Evaluación de archivado

[Índice ES](../../README.es.md) · [Index EN](../../README.md)

## Caso profesional

**Estado:** Evaluación y diseño.

Evaluación de aproximadamente 11,7 TB en OneDrive y SharePoint. El volumen analizado no representa datos migrados; ahorro y elegibilidad pendientes de validar.

**Tecnologías del caso:** Microsoft 365 · OneDrive · SharePoint · Graph · PowerShell.

[Fuente pública](https://www.linkedin.com/feed/update/urn:li:activity:7501147613795164160/) · Proyecto de LinkedIn `346928500`. El título de esta ficha permite localizar el caso en el perfil.

## Demostración con datos ficticios

Selecciona candidatos según fecha de actividad, retención y retenciones legales, separando exclusiones.

```text
Inventory → date criteria → legal/retention exclusions → candidate list
```

```sh
# Desde cloud-security-automation; Python 3.11+, biblioteca estándar.
python3 demo.py data-lifecycle
python3 demo.py data-lifecycle --output generated/data-lifecycle.json
```

[Datos de entrada](input.json) · [Salida de muestra](output.example.json) · [Implementación: `archive_candidates`](../../lab/cloud.py) · [Pruebas](../../tests/test_catalog.py)

**Límite del ejemplo:** No decide políticas de conservación, mueve archivos ni calcula ahorros. La selección requiere revisión del dueño de la información.

Los datos se crearon desde cero para este portafolio. El código es una reconstrucción demostrativa preparada con asistencia de IA a partir de la descripción del caso. Los resultados sintéticos no acreditan métricas de producción ni amplían el estado del proyecto profesional.

## English

**Microsoft 365 data lifecycle and archive assessment** — Assessment and design.

Assessment of approximately 11.7 TB in OneDrive and SharePoint. This is analyzed volume, not migrated data; savings and eligibility remain unvalidated.

**Demonstration:** Selects candidates by activity date, retention and legal holds, recording exclusions.

**Boundary:** Does not decide retention policy, move files or calculate savings. Selection requires information-owner review.

Run the commands above from the package directory. The fixture and output are synthetic; the code is an AI-assisted illustrative reconstruction, not production evidence. See the [data policy](../../docs/data-policy.md).
