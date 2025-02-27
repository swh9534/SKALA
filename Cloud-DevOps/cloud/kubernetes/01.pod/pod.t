apiVersion: v1
kind: Pod
metadata:
  name: ${USER_NAME}-${SERVICE_NAME}
  namespace: ${NAMESPACE}
  labels:
    app: ${USER_NAME}-${SERVICE_NAME}
spec:
  serviceAccountName: default
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: ${TAINT_KEY}
            operator: In
            values:
            - "${TAINT_VALUE}"
  containers:
  - name: nginx
    image:  ${IMAGE_NAME}:${VERSION}
    imagePullPolicy: Always
    env:
    - name: USER_NAME
      value: ${USER_NAME}
  tolerations:
  - effect: ${TAINT_EFFECT}
    key: ${TAINT_KEY}
    operator: Equal
    value: "${TAINT_VALUE}"
