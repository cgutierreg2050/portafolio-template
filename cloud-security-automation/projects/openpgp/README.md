# 17. Intercambio seguro de archivos | OpenPGP, SFTP y PowerShell

[Índice ES](../../README.es.md) · [Index EN](../../README.md)

## Caso profesional

**Estado:** Desarrollo y validación.

Identificación de subclaves y diagnóstico de contextos interactivo/SYSTEM realizados; automatización completa en validación.

**Tecnologías del caso:** GnuPG · SFTP · WinSCP · PowerShell · Linux · Windows.

[Fuente pública](https://www.linkedin.com/feed/update/urn:li:activity:7501148513687224320/) · Proyecto de LinkedIn `256155060`. El título de esta ficha permite localizar el caso en el perfil.

## Demostración con datos ficticios

Compara metadatos de subclave, contexto de ejecución, expiración y revocación.

```text
Recipient metadata → key/context checks → readiness reasons
```

```sh
# Desde cloud-security-automation; Python 3.11+, biblioteca estándar.
python3 demo.py openpgp
python3 demo.py openpgp --output generated/openpgp.json
```

[Datos de entrada](input.json) · [Salida de muestra](output.example.json) · [Implementación: `pgp_context`](../../lab/security.py) · [Pruebas](../../tests/test_catalog.py)

**Límite del ejemplo:** No almacena claves privadas, interpreta paquetes OpenPGP, descifra ni transfiere archivos.

Los datos se crearon desde cero para este portafolio. El código es una reconstrucción demostrativa preparada con asistencia de IA a partir de la descripción del caso. Los resultados sintéticos no acreditan métricas de producción ni amplían el estado del proyecto profesional.

## English

**Secure file exchange with OpenPGP and SFTP** — Development and validation.

Recipient subkey and interactive/SYSTEM context diagnostics completed; end-to-end automation remains under validation.

**Demonstration:** Checks subkey metadata, execution context, expiry and revocation.

**Boundary:** No private keys, OpenPGP packet parsing, decryption or file transfer.

Run the commands above from the package directory. The fixture and output are synthetic; the code is an AI-assisted illustrative reconstruction, not production evidence. See the [data policy](../../docs/data-policy.md).
