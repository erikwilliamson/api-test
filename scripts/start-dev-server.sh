#!/bin/bash

set -e

# Exit Codes
E_OK=0
E_USAGE=1

# Directories and Files
SCRIPT_NAME=$(basename $0)
SCRIPTS_DIR=$(dirname $0)
BASE_DIR=$(readlink -f "${SCRIPTS_DIR}/..")
VIRTUAL_ENV_DIR=$(poetry env info -p)
ACTIVATE_SCRIPT="${VIRTUAL_ENV_DIR}/bin/activate"
ENV_FILE="${BASE_DIR}/.env"

# Application Configs
API_HOST=$(< "${ENV_FILE}" grep -E "^API_HOST" | cut -d "=" -f 2)
API_PORT=$(< "${ENV_FILE}" grep -E "^API_PORT" | cut -d "=" -f 2)
RELOAD=$(< "${ENV_FILE}" grep -E "^RELOAD" | cut -d "=" -f 2)

if [[ ${RELOAD} == "True" || ${RELOAD} == "TRUE" || ${RELOAD} == "true" ]] ; then
  RELOAD="--reload"
else
  RELOAD=""
fi

if [[ -z "${VIRTUAL_ENV}" ]] ; then
  echo "Activating VirtualEnv ${VIRTUAL_ENV}"
  if [[ -e ${ACTIVATE_SCRIPT} ]] ; then
    # shellcheck source=/Users/erik/Library/Caches/pypoetry/virtualenvs/app-1hNXwqP_-py3.10/bin/activate
    source "${ACTIVATE_SCRIPT}"
  fi
fi

echo "API_HOST: ${API_HOST}"
echo "API_PORT: ${API_PORT}"
echo "RELOAD: ${RELOAD}"

uvicorn app.main:app "${RELOAD}" --host "${API_HOST}" --port "${API_PORT}"

exit ${E_OK}