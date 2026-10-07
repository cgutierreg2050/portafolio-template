# 14. Hardening post-incidente en Microsoft 365

[Índice ES](../../README.es.md) · [Index EN](../../README.md)

## Caso profesional

**Estado:** Implementado, según el caso publicado.

Recuperación y fortalecimiento de un tenant: revisión de identidades privilegiadas, reglas de reenvío, MFA y acceso condicional.

**Tecnologías del caso:** Microsoft 365 · Entra ID · MFA · Conditional Access · PowerShell.

[Fuente pública](https://www.linkedin.com/in/kristiangutierrez/details/projects/) · Proyecto de LinkedIn `433649684`. El título de esta ficha permite localizar el caso en el perfil.

## Demostración con datos ficticios

Genera hallazgos sobre administradores no aprobados, carencias de MFA y reenvíos externos no autorizados.

```text
Identity/rule snapshot → read-only checks → prioritized findings
```

```sh
# Desde cloud-security-automation; Python 3.11+, biblioteca estándar.
python3 demo.py m365-hardening
python3 demo.py m365-hardening --output generated/m365-hardening.json
```

[Datos de entrada](input.json) · [Salida de muestra](output.example.json) · [Implementación: `hardening`](../../lab/security.py) · [Pruebas](../../tests/test_catalog.py)

**Límite del ejemplo:** No elimina cuentas, revoca sesiones ni altera el tenant. Los hallazgos requieren revisión contextual.

Los datos se crearon desde cero para este portafolio. El código es una reconstrucción demostrativa preparada con asistencia de IA a partir de la descripción del caso. Los resultados sintéticos no acreditan métricas de producción ni amplían el estado del proyecto profesional.

## English

**Post-incident Microsoft 365 hardening** — Implemented, as described in the published case.

Tenant recovery and hardening through privileged-identity review, forwarding-rule review, MFA and conditional access.

**Demonstration:** Reports unapproved administrators, MFA gaps and unapproved external forwarding.

**Boundary:** Does not delete accounts, revoke sessions or alter a tenant. Findings need contextual review.

Run the commands above from the package directory. The fixture and output are synthetic; the code is an AI-assisted illustrative reconstruction, not production evidence. See the [data policy](../../docs/data-policy.md).
