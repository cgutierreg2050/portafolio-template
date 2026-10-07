# Datos y procedencia / Data and provenance

## Español

Los datos de las 25 demostraciones se crearon **desde cero**. No se descargaron inventarios empresariales, exportaciones de tenants, correos, expedientes, audio, claves ni registros de producción para generar estos ejemplos.

- Nombres e identificadores usan etiquetas `DEMO`, `demo` o nombres genéricos.
- Direcciones de correo y dominios de las muestras usan `example.test`.
- Las redes de ejemplo usan `192.0.2.0/24` y `198.51.100.0/24`, reservadas para documentación.
- CVE, KB, hashes, claves y referencias de secretos son marcadores inventados. No son indicadores reales ni material criptográfico.
- `synthetic: true` declara la procedencia del archivo; no anonimiza datos reales.
- La documentación profesional puede incluir métricas ya publicadas por el propietario. Las cifras de los fixtures son independientes.

El código fue reconstruido con asistencia de IA para mostrar una parte de cada problema. Las fichas identifican explícitamente qué demuestra y qué no implementa cada ejemplo. El código no realiza llamadas a Azure, Microsoft Graph, Action1, Cloudflare, correo ni infraestructura empresarial. Las demostraciones nuevas solo leen JSON local y producen resultados locales.

Las pruebas comprueban las muestras incluidas y algunos límites de comportamiento. La revisión de nombres y dominios es una comprobación acotada, no una garantía universal de anonimización. Si se aportan nuevos datos, deben ser sintéticos y revisarse antes de publicar; quitar un nombre no basta para anonimizar una exportación.

## English

All 25 fixtures were authored from scratch. No enterprise exports, tenant inventories, real messages, legal files, recordings, keys or production logs were used to produce them. Demo domains, documentation address ranges and clearly fictional identifiers keep the sample data separate from professional case metrics.

`synthetic: true` is a declaration, not an anonymizer. The examples are AI-assisted illustrative reconstructions, with specific boundaries documented per case. New labs only read local JSON and return local results. Tests cover the shipped fixtures and selected behavior; they are not a universal privacy detector or production certification.
