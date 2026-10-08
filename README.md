# Sistema de Triage de Mensajes — Atlas Academy
## ¿Qué hace?
Este sistema analiza todos los mensajes enviados mediante el canal de soporte y los diferencia por urgencia y categorías diferentes

## ¿Cómo funciona?
1. Si la urgencia es alta, se guarda el ticket y queda marcado para una revisión de alta urgencia que se tiene que revisar con prioridad
2. Las otras simplemente pasarán a un registro normal para que puedan ser vistas con un tiempo más prolongado

## ¿Qué necesita mi equipo para usarlo?
El cliente necesitaría una parte de soporte como un formulario o un chat donde se pueda mandar un mensaje y conectar estos mensajes para poder catalogarlos y darles su respectiva urgencia


## ¿Qué pasa si algo falla?
Se guardan en un sitio donde se tienen que revisar a mano ya que aún no hay procesamiento automático

## ¿Qué problema resuelve?

Este sistema reduce el tiempo que el equipo de soporte necesita para revisar y clasificar manualmente los mensajes recibidos.

En lugar de revisar cada mensaje desde cero, el equipo recibe los mensajes ya clasificados según su urgencia y categoría, permitiendo dedicar más tiempo a los casos que realmente necesitan intervención.


## ¿Qué puede ahorrar?

Por ejemplo, si una empresa recibe 100 mensajes al mes y cada mensaje tarda aproximadamente 3 minutos en revisarse y clasificarse:
100 mensajes × 3 minutos = 300 minutos
Eso supone aproximadamente 5 horas de trabajo al mes únicamente en clasificación.
Si el sistema automatiza esta primera clasificación, esas horas pueden dedicarse a tareas de mayor valor.

## ¿Para quién está pensado?

Especialmente para empresas que:

- Reciben muchos mensajes de soporte.
- Tienen que revisar y clasificar tickets manualmente.
- Necesitan detectar rápidamente incidencias urgentes.
- Quieren reducir tareas repetitivas de su equipo.

## Limitaciones actuales

Actualmente el sistema:

- Clasifica y prioriza los mensajes.
- Marca los casos de alta urgencia.
- Mantiene un registro de los casos.
- Envía los casos que no puede procesar a revisión manual.

## Preguntas Frecuentes

### ¿Por qué necesito esto si ya tengo personal para revisar los mensajes?
Puede ser una herramienta útil para apoyar al personal. Pueden darse casos donde el personal tenga tiempo limitado o reciba una cantidad excesiva de mensajes y no pueda clasificarlos todos al mismo tiempo. Este sistema ahorra tiempo en ese aspecto y asegura que ningún mensaje se pierda, aunque algunos puedan quedar pendientes de clasificación en caso de fallo.

### ¿Qué pasa si la IA clasifica mal un mensaje?
Aunque un mensaje esté mal clasificado, el personal solo tiene que revisar la clasificación, no leer y categorizar el mensaje desde cero. Esto ahorra tiempo: en vez de analizar cada mensaje por completo, solo hay que confirmar rápidamente si la categoría asignada tiene sentido.

### ¿Gemini guarda la información de los mensajes?
Gemini guarda esta información durante 55 días para control de uso, según sus políticas. Google no usa esos datos para entrenar sus modelos, y pasado ese periodo la información se elimina.

## Tecnologías utilizadas
Python: lógica del sistema y procesamiento de los tickets.
FastAPI: API que recibe los mensajes y devuelve su clasificación.
Gemini: análisis del contenido mediante inteligencia artificial para determinar la categoría, la urgencia, el sentimiento y un resumen del mensaje.
n8n: automatización del flujo de trabajo y gestión de las decisiones según la urgencia detectada.
JSONL: almacenamiento del historial de tickets procesados.

## Flujo de procesamiento
El sistema recibe un mensaje de soporte.
La IA analiza su contenido y genera una clasificación estructurada.
La API devuelve los datos del ticket, incluyendo su categoría, urgencia, sentimiento y resumen.
n8n evalúa la urgencia y dirige el ticket al flujo correspondiente.
El ticket queda registrado para su consulta posterior. Los casos que requieren atención prioritaria se identifican para facilitar su revisión.