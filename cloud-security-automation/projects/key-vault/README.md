# 02. Migración automatizada a Azure Key Vault | 187 secretos

[Índice ES](../../README.es.md) · [Index EN](../../README.md)

## Caso profesional

**Estado:** Implementado, según el caso publicado.

Migración documentada de 187 secretos, con cero errores y cero elementos omitidos; incluyó validación de acceso, simulación y reporte.

**Tecnologías del caso:** PowerShell · KPScript · Azure Key Vault · Azure RBAC.

[Fuente pública](https://www.linkedin.com/feed/update/urn:li:activity:7489850755160489984/) · Proyecto de LinkedIn `172811513`. El título de esta ficha permite localizar el caso en el perfil.

## Demostración con datos ficticios

Normaliza nombres de entradas ficticias y rechaza colisiones o campos que puedan contener credenciales.

```text
Metadata → name validation → collision check → proposed plan
```

```sh
# Desde cloud-security-automation; Python 3.11+, biblioteca estándar.
python3 demo.py key-vault
python3 demo.py key-vault --output generated/key-vault.json
```

[Datos de entrada](input.json) · [Salida de muestra](output.example.json) · [Implementación: `key_vault_plan`](../../lab/security.py) · [Pruebas](../../tests/test_catalog.py)

Alternativa PowerShell: [plan.ps1](../../examples/key-vault-plan/plan.ps1).

**Límite del ejemplo:** Solo procesa id y título; no lee KeePass, valores de secretos ni llama a Azure. Los tres registros de muestra no representan la migración real.

Los datos se crearon desde cero para este portafolio. El código es una reconstrucción demostrativa preparada con asistencia de IA a partir de la descripción del caso. Los resultados sintéticos no acreditan métricas de producción ni amplían el estado del proyecto profesional.

## English

**KeePass to Azure Key Vault migration** — Implemented, as described in the published case.

Documented migration of 187 secrets, zero errors and zero skipped entries, with access checks, a dry run and reporting.

**Demonstration:** Normalizes synthetic entry names and rejects collisions or fields that could contain credentials.

**Boundary:** Metadata only; no KeePass access, secret values or Azure calls. The three fixture entries do not represent the real migration.

Run the commands above from the package directory. The fixture and output are synthetic; the code is an AI-assisted illustrative reconstruction, not production evidence. See the [data policy](../../docs/data-policy.md).
