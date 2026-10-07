# 24. Recuperación de VM Windows y diagnóstico por capas | KVM/QEMU

[Índice ES](../../README.es.md) · [Index EN](../../README.md)

## Caso profesional

**Estado:** Arranque y acceso a consola recuperados.

Recuperación de arranque corrigiendo ruta QCOW2 y uso de consola/noVNC. También se identificó un problema de confianza AD; su resolución no se afirma.

**Tecnologías del caso:** KVM/QEMU · libvirt · Linux · Windows · noVNC · Websockify.

[Fuente pública](https://www.linkedin.com/feed/update/urn:li:activity:7495990357336424448/) · Proyecto de LinkedIn `346880371`. El título de esta ficha permite localizar el caso en el perfil.

## Demostración con datos ficticios

Inspecciona XML ficticio y propone revisar una ruta de disco solo si existe un candidato inequívoco.

```text
Libvirt XML + disk inventory → path match → ambiguity check → recovery checklist
```

```sh
# Desde cloud-security-automation; Python 3.11+, biblioteca estándar.
python3 demo.py kvm-recovery
python3 demo.py kvm-recovery --output generated/kvm-recovery.json
```

[Datos de entrada](input.json) · [Salida de muestra](output.example.json) · [Implementación: `kvm_recovery`](../../lab/operations.py) · [Pruebas](../../tests/test_catalog.py)

**Límite del ejemplo:** No abre discos, modifica libvirt ni inicia VM. No evita BitLocker ni resuelve confianza del dominio.

Los datos se crearon desde cero para este portafolio. El código es una reconstrucción demostrativa preparada con asistencia de IA a partir de la descripción del caso. Los resultados sintéticos no acreditan métricas de producción ni amplían el estado del proyecto profesional.

## English

**KVM/QEMU Windows VM recovery** — VM startup and console access restored.

Startup restored by correcting a QCOW2 path, with console/noVNC access. An AD trust issue was identified; its resolution is not claimed.

**Demonstration:** Inspects synthetic XML and proposes a disk path only when there is one unambiguous candidate.

**Boundary:** Does not open disks, modify libvirt or start VMs. Does not bypass BitLocker or resolve domain trust.

Run the commands above from the package directory. The fixture and output are synthetic; the code is an AI-assisted illustrative reconstruction, not production evidence. See the [data policy](../../docs/data-policy.md).
