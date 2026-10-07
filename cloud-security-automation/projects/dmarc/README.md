# 01. Seguridad de correo y diagnóstico de DMARC | Exchange Online

[Índice ES](../../README.es.md) · [Index EN](../../README.md)

## Caso profesional

**Estado:** Implementado, según el caso publicado.

Diagnóstico de fallos de reenvío entre organizaciones y aplicación de una excepción acotada al flujo legítimo, conservando la protección contra suplantación.

**Tecnologías del caso:** Exchange Online · Microsoft Defender · PowerShell · SPF/DKIM/DMARC.

[Fuente pública](https://www.linkedin.com/feed/update/urn:li:activity:7501146655493128193/) · Proyecto de LinkedIn `256361184`. El título de esta ficha permite localizar el caso en el perfil.

## Demostración con datos ficticios

Evalúa alineación estricta de SPF y DKIM con el dominio From a partir de resultados ficticios.

```text
Headers → strict alignment → forwarding review → report
```

```sh
# Desde cloud-security-automation; Python 3.11+, biblioteca estándar.
python3 demo.py dmarc
python3 demo.py dmarc --output generated/dmarc.json
```

[Datos de entrada](input.json) · [Salida de muestra](output.example.json) · [Implementación: `dmarc`](../../lab/security.py) · [Pruebas](../../tests/test_catalog.py)

**Límite del ejemplo:** No consulta DNS, valida firmas ni implementa alineación relajada o ARC. Un resultado de revisión no autoriza al remitente.

Los datos se crearon desde cero para este portafolio. El código es una reconstrucción demostrativa preparada con asistencia de IA a partir de la descripción del caso. Los resultados sintéticos no acreditan métricas de producción ni amplían el estado del proyecto profesional.

## English

**Email security and DMARC diagnostics** — Implemented, as described in the published case.

Diagnosed cross-organization forwarding failures and applied a scoped exception while preserving anti-spoofing controls.

**Demonstration:** Evaluates strict SPF/DKIM domain alignment against the From domain using supplied synthetic results.

**Boundary:** No DNS queries, signature verification, relaxed alignment or ARC. A review finding does not allowlist a sender.

Run the commands above from the package directory. The fixture and output are synthetic; the code is an AI-assisted illustrative reconstruction, not production evidence. See the [data policy](../../docs/data-policy.md).
