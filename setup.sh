#!/usr/bin/env bash

LESSON_NUM="${1}"
LESSON_DIR="lesson-${LESSON_NUM}"

TASK_TEMPLATE="templates/task_template.py"
TASKS_COUNT="${2}"

_check_args() {
  if [[ -z "${LESSON_NUM}" ]]; then
    echo "Parameter '\${LESSON_NUM}' is not defined"
    exit 1
  elif [[ -z "${TASKS_COUNT}" ]]; then
    echo "Parameter '\${TASKS_COUNT}' is not defined"
    exit 1
  fi
}

_create_lesson_dir() {
  mkdir -p "${LESSON_DIR}"
}

_create_tasks() {
  for ((i = 1; i <= ${1}; i++)); do
    cp -f "${TASK_TEMPLATE}" "${LESSON_DIR}/task$(printf "%02d" ${i}).py"
  done
}

_main() {
  _check_args
  _create_lesson_dir "${LESSON_NUM}"
  _create_tasks "${TASKS_COUNT}"
}

# Entrypoint
_main "${*}"
