# 19. Migración de prueba y validación de inventario | GLPI y Defender

[Índice ES](../../README.es.md) · [Index EN](../../README.md)

## Caso profesional

**Estado:** Migración probada en entorno de prueba.

Prueba de GLPI 10.0.15 a 11.0.11 con PHP 8.2 y base independiente; validación del inventario frente al estado real de Defender.

**Tecnologías del caso:** GLPI · PHP · Defender for Endpoint · PowerShell · Action1.

[Fuente pública](https://www.linkedin.com/feed/update/urn:li:activity:7513107296491638785/) · Proyecto de LinkedIn `255879886`. El título de esta ficha permite localizar el caso en el perfil.

## Demostración con datos ficticios

Compara conjuntos de tablas y separa errores de inventario, carencias de protección y firmas antiguas.

```text
Schema snapshots + endpoint state → comparison → categorized findings
```

```sh
# Desde cloud-security-automation; Python 3.11+, biblioteca estándar.
python3 demo.py glpi-defender
python3 demo.py glpi-defender --output generated/glpi-defender.json
```

[Datos de entrada](input.json) · [Salida de muestra](output.example.json) · [Implementación: `glpi_inventory`](../../lab/operations.py) · [Pruebas](../../tests/test_catalog.py)

**Límite del ejemplo:** No restaura bases, ejecuta migraciones ni modifica GLPI Agent. La comparación de tablas no demuestra integridad completa del esquema.

Los datos se crearon desde cero para este portafolio. El código es una reconstrucción demostrativa preparada con asistencia de IA a partir de la descripción del caso. Los resultados sintéticos no acreditan métricas de producción ni amplían el estado del proyecto profesional.

## English

**GLPI test migration and Defender inventory validation** — Migration tested in a test environment.

GLPI 10.0.15 to 11.0.11 test with PHP 8.2 and an independent database; inventory validation against actual Defender status.

**Demonstration:** Compares table sets and distinguishes inventory mismatches, protection gaps and stale signatures.

**Boundary:** No database restore, migration or GLPI Agent changes. Table comparison does not prove full schema integrity.

Run the commands above from the package directory. The fixture and output are synthetic; the code is an AI-assisted illustrative reconstruction, not production evidence. See the [data policy](../../docs/data-policy.md).
