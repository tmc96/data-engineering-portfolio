{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tW_5k-nRx7cl",
        "outputId": "fc1c3ce9-82f7-45dd-9504-b9c3dbb91026"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[?25l     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m0.0/43.7 kB\u001b[0m \u001b[31m?\u001b[0m eta \u001b[36m-:--:--\u001b[0m\r\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m43.7/43.7 kB\u001b[0m \u001b[31m1.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "\u001b[33mWARNING: connexion 2.15.1 does not provide the extra 'flask'\u001b[0m\u001b[33m\n",
            "\u001b[0m\u001b[33mWARNING: connexion 2.15.0 does not provide the extra 'flask'\u001b[0m\u001b[33m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m13.3/13.3 MB\u001b[0m \u001b[31m106.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m98.1/98.1 kB\u001b[0m \u001b[31m6.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m2.2/2.2 MB\u001b[0m \u001b[31m77.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m43.8/43.8 kB\u001b[0m \u001b[31m2.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m95.1/95.1 kB\u001b[0m \u001b[31m8.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m74.4/74.4 kB\u001b[0m \u001b[31m6.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m101.8/101.8 kB\u001b[0m \u001b[31m7.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m591.3/591.3 kB\u001b[0m \u001b[31m35.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m85.0/85.0 kB\u001b[0m \u001b[31m7.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m351.2/351.2 kB\u001b[0m \u001b[31m22.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m1.6/1.6 MB\u001b[0m \u001b[31m71.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m80.7/80.7 kB\u001b[0m \u001b[31m5.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m233.6/233.6 kB\u001b[0m \u001b[31m14.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m63.9/63.9 kB\u001b[0m \u001b[31m4.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m71.5/71.5 kB\u001b[0m \u001b[31m5.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m72.5/72.5 kB\u001b[0m \u001b[31m5.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m51.0/51.0 kB\u001b[0m \u001b[31m3.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m152.5/152.5 kB\u001b[0m \u001b[31m10.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m132.6/132.6 kB\u001b[0m \u001b[31m9.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m66.4/66.4 kB\u001b[0m \u001b[31m3.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m220.0/220.0 kB\u001b[0m \u001b[31m16.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m91.8/91.8 kB\u001b[0m \u001b[31m7.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m331.1/331.1 kB\u001b[0m \u001b[31m19.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m60.6/60.6 kB\u001b[0m \u001b[31m4.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h  Building wheel for python-nvd3 (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Building wheel for unicodecsv (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "\u001b[31mERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.\n",
            "opentelemetry-exporter-gcp-logging 1.11.0a0 requires opentelemetry-sdk<1.39.0,>=1.35.0, but you have opentelemetry-sdk 1.39.1 which is incompatible.\n",
            "google-adk 1.21.0 requires opentelemetry-api<=1.37.0,>=1.37.0, but you have opentelemetry-api 1.39.1 which is incompatible.\n",
            "google-adk 1.21.0 requires opentelemetry-sdk<=1.37.0,>=1.37.0, but you have opentelemetry-sdk 1.39.1 which is incompatible.\n",
            "google-adk 1.21.0 requires sqlalchemy<3.0.0,>=2.0, but you have sqlalchemy 1.4.54 which is incompatible.\n",
            "ipython-sql 0.5.0 requires sqlalchemy>=2.0, but you have sqlalchemy 1.4.54 which is incompatible.\u001b[0m\u001b[31m\n",
            "\u001b[0m"
          ]
        }
      ],
      "source": [
        "!pip install apache-airflow==2.9.1 --quiet"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Initialize Airflow DB\n",
        "!airflow db init"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ICd7r8cPyLi8",
        "outputId": "109c5f7b-7d67-41fd-c0e4-fc80a8304c75"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "DB: sqlite:////root/airflow/airflow.db\n",
            "[\u001b[34m2026-01-02T19:01:43.382+0000\u001b[0m] {\u001b[34mmigration.py:\u001b[0m211} INFO\u001b[0m - Context impl \u001b[01mSQLiteImpl\u001b[22m.\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:01:43.386+0000\u001b[0m] {\u001b[34mmigration.py:\u001b[0m214} INFO\u001b[0m - Will assume \u001b[01mnon-transactional\u001b[22m DDL.\u001b[0m\n",
            "INFO  [alembic.runtime.migration] Context impl SQLiteImpl.\n",
            "INFO  [alembic.runtime.migration] Will assume non-transactional DDL.\n",
            "INFO  [alembic.runtime.migration] Running stamp_revision  -> 1949afb29106\n",
            "WARNI [airflow.models.crypto] empty cryptography key - values will not be stored encrypted.\n",
            "Initialization done\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# STEP 1: Set up directories\n",
        "# ----------------------------\n",
        "# Paths\n",
        "import os\n",
        "DAGS_PATH = os.path.expanduser('~/airflow/dags')\n",
        "DATA_PATH = os.path.expanduser('~/airflow/data/cleaned&transformed_fmcg_data.csv')\n",
        "OUTPUT_SUMMARY_PATH = os.path.expanduser('~/airflow/data/output_summary.csv')\n",
        "OUTPUT_AGG_PATH = os.path.expanduser('~/airflow/data/output_agg.csv')\n",
        "\n",
        "# Make sure folders exist\n",
        "os.makedirs(DAGS_PATH, exist_ok=True)\n",
        "os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)\n",
        "os.makedirs(os.path.dirname(OUTPUT_SUMMARY_PATH), exist_ok=True)\n",
        "os.makedirs(os.path.dirname(OUTPUT_AGG_PATH), exist_ok=True)\n"
      ],
      "metadata": {
        "id": "Vyl0KHY46mJq"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# STEP 2: Upload CSV in Colab\n",
        "# ----------------------------\n",
        "from google.colab import files\n",
        "import shutil\n",
        "\n",
        "uploaded = files.upload()  # Upload cleaned&transformed_fmcg_data.csv here\n",
        "\n",
        "for fname in uploaded.keys():\n",
        "    # Move the uploaded file to Airflow data directory\n",
        "    shutil.move(fname, DATA_PATH)\n",
        "    print(f\"Uploaded {fname} to {DATA_PATH}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 90
        },
        "id": "5R4tttR-6svM",
        "outputId": "3fd36f94-dffb-4a52-e878-be2865d091d4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "\n",
              "     <input type=\"file\" id=\"files-6ba2fc0a-d381-4d0a-975c-5ec0f1de3800\" name=\"files[]\" multiple disabled\n",
              "        style=\"border:none\" />\n",
              "     <output id=\"result-6ba2fc0a-d381-4d0a-975c-5ec0f1de3800\">\n",
              "      Upload widget is only available when the cell has been executed in the\n",
              "      current browser session. Please rerun this cell to enable.\n",
              "      </output>\n",
              "      <script>// Copyright 2017 Google LLC\n",
              "//\n",
              "// Licensed under the Apache License, Version 2.0 (the \"License\");\n",
              "// you may not use this file except in compliance with the License.\n",
              "// You may obtain a copy of the License at\n",
              "//\n",
              "//      http://www.apache.org/licenses/LICENSE-2.0\n",
              "//\n",
              "// Unless required by applicable law or agreed to in writing, software\n",
              "// distributed under the License is distributed on an \"AS IS\" BASIS,\n",
              "// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n",
              "// See the License for the specific language governing permissions and\n",
              "// limitations under the License.\n",
              "\n",
              "/**\n",
              " * @fileoverview Helpers for google.colab Python module.\n",
              " */\n",
              "(function(scope) {\n",
              "function span(text, styleAttributes = {}) {\n",
              "  const element = document.createElement('span');\n",
              "  element.textContent = text;\n",
              "  for (const key of Object.keys(styleAttributes)) {\n",
              "    element.style[key] = styleAttributes[key];\n",
              "  }\n",
              "  return element;\n",
              "}\n",
              "\n",
              "// Max number of bytes which will be uploaded at a time.\n",
              "const MAX_PAYLOAD_SIZE = 100 * 1024;\n",
              "\n",
              "function _uploadFiles(inputId, outputId) {\n",
              "  const steps = uploadFilesStep(inputId, outputId);\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  // Cache steps on the outputElement to make it available for the next call\n",
              "  // to uploadFilesContinue from Python.\n",
              "  outputElement.steps = steps;\n",
              "\n",
              "  return _uploadFilesContinue(outputId);\n",
              "}\n",
              "\n",
              "// This is roughly an async generator (not supported in the browser yet),\n",
              "// where there are multiple asynchronous steps and the Python side is going\n",
              "// to poll for completion of each step.\n",
              "// This uses a Promise to block the python side on completion of each step,\n",
              "// then passes the result of the previous step as the input to the next step.\n",
              "function _uploadFilesContinue(outputId) {\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  const steps = outputElement.steps;\n",
              "\n",
              "  const next = steps.next(outputElement.lastPromiseValue);\n",
              "  return Promise.resolve(next.value.promise).then((value) => {\n",
              "    // Cache the last promise value to make it available to the next\n",
              "    // step of the generator.\n",
              "    outputElement.lastPromiseValue = value;\n",
              "    return next.value.response;\n",
              "  });\n",
              "}\n",
              "\n",
              "/**\n",
              " * Generator function which is called between each async step of the upload\n",
              " * process.\n",
              " * @param {string} inputId Element ID of the input file picker element.\n",
              " * @param {string} outputId Element ID of the output display.\n",
              " * @return {!Iterable<!Object>} Iterable of next steps.\n",
              " */\n",
              "function* uploadFilesStep(inputId, outputId) {\n",
              "  const inputElement = document.getElementById(inputId);\n",
              "  inputElement.disabled = false;\n",
              "\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  outputElement.innerHTML = '';\n",
              "\n",
              "  const pickedPromise = new Promise((resolve) => {\n",
              "    inputElement.addEventListener('change', (e) => {\n",
              "      resolve(e.target.files);\n",
              "    });\n",
              "  });\n",
              "\n",
              "  const cancel = document.createElement('button');\n",
              "  inputElement.parentElement.appendChild(cancel);\n",
              "  cancel.textContent = 'Cancel upload';\n",
              "  const cancelPromise = new Promise((resolve) => {\n",
              "    cancel.onclick = () => {\n",
              "      resolve(null);\n",
              "    };\n",
              "  });\n",
              "\n",
              "  // Wait for the user to pick the files.\n",
              "  const files = yield {\n",
              "    promise: Promise.race([pickedPromise, cancelPromise]),\n",
              "    response: {\n",
              "      action: 'starting',\n",
              "    }\n",
              "  };\n",
              "\n",
              "  cancel.remove();\n",
              "\n",
              "  // Disable the input element since further picks are not allowed.\n",
              "  inputElement.disabled = true;\n",
              "\n",
              "  if (!files) {\n",
              "    return {\n",
              "      response: {\n",
              "        action: 'complete',\n",
              "      }\n",
              "    };\n",
              "  }\n",
              "\n",
              "  for (const file of files) {\n",
              "    const li = document.createElement('li');\n",
              "    li.append(span(file.name, {fontWeight: 'bold'}));\n",
              "    li.append(span(\n",
              "        `(${file.type || 'n/a'}) - ${file.size} bytes, ` +\n",
              "        `last modified: ${\n",
              "            file.lastModifiedDate ? file.lastModifiedDate.toLocaleDateString() :\n",
              "                                    'n/a'} - `));\n",
              "    const percent = span('0% done');\n",
              "    li.appendChild(percent);\n",
              "\n",
              "    outputElement.appendChild(li);\n",
              "\n",
              "    const fileDataPromise = new Promise((resolve) => {\n",
              "      const reader = new FileReader();\n",
              "      reader.onload = (e) => {\n",
              "        resolve(e.target.result);\n",
              "      };\n",
              "      reader.readAsArrayBuffer(file);\n",
              "    });\n",
              "    // Wait for the data to be ready.\n",
              "    let fileData = yield {\n",
              "      promise: fileDataPromise,\n",
              "      response: {\n",
              "        action: 'continue',\n",
              "      }\n",
              "    };\n",
              "\n",
              "    // Use a chunked sending to avoid message size limits. See b/62115660.\n",
              "    let position = 0;\n",
              "    do {\n",
              "      const length = Math.min(fileData.byteLength - position, MAX_PAYLOAD_SIZE);\n",
              "      const chunk = new Uint8Array(fileData, position, length);\n",
              "      position += length;\n",
              "\n",
              "      const base64 = btoa(String.fromCharCode.apply(null, chunk));\n",
              "      yield {\n",
              "        response: {\n",
              "          action: 'append',\n",
              "          file: file.name,\n",
              "          data: base64,\n",
              "        },\n",
              "      };\n",
              "\n",
              "      let percentDone = fileData.byteLength === 0 ?\n",
              "          100 :\n",
              "          Math.round((position / fileData.byteLength) * 100);\n",
              "      percent.textContent = `${percentDone}% done`;\n",
              "\n",
              "    } while (position < fileData.byteLength);\n",
              "  }\n",
              "\n",
              "  // All done.\n",
              "  yield {\n",
              "    response: {\n",
              "      action: 'complete',\n",
              "    }\n",
              "  };\n",
              "}\n",
              "\n",
              "scope.google = scope.google || {};\n",
              "scope.google.colab = scope.google.colab || {};\n",
              "scope.google.colab._files = {\n",
              "  _uploadFiles,\n",
              "  _uploadFilesContinue,\n",
              "};\n",
              "})(self);\n",
              "</script> "
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Saving cleaned&transformed_fmcg_data.csv to cleaned&transformed_fmcg_data.csv\n",
            "Uploaded cleaned&transformed_fmcg_data.csv to /root/airflow/data/cleaned&transformed_fmcg_data.csv\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "\n",
        "DAGS_PATH = os.path.expanduser('~/airflow/dags')\n",
        "os.makedirs(DAGS_PATH, exist_ok=True)\n",
        "\n",
        "dag_file_path = os.path.join(DAGS_PATH, \"fmcg_pipeline.py\")\n",
        "\n",
        "dag_code = \"\"\"\n",
        "from airflow import DAG\n",
        "from airflow.operators.python import PythonOperator\n",
        "from datetime import datetime\n",
        "import pandas as pd\n",
        "import os\n",
        "\n",
        "DATA_PATH = os.path.expanduser('~/airflow/data/cleaned&transformed_fmcg_data.csv')\n",
        "OUTPUT_DIR = os.path.expanduser('~/airflow/data')\n",
        "\n",
        "os.makedirs(OUTPUT_DIR, exist_ok=True)\n",
        "\n",
        "def sales_by_product():\n",
        "    df = pd.read_csv(DATA_PATH)\n",
        "    result = (\n",
        "        df.groupby('product_name')['final_amount']\n",
        "        .sum()\n",
        "        .reset_index()\n",
        "        .sort_values(by='final_amount', ascending=False)\n",
        "    )\n",
        "    result.to_csv(os.path.join(OUTPUT_DIR, 'sales_by_product.csv'), index=False)\n",
        "\n",
        "def sales_by_store():\n",
        "    df = pd.read_csv(DATA_PATH)\n",
        "    result = (\n",
        "        df.groupby('store_name')['final_amount']\n",
        "        .sum()\n",
        "        .reset_index()\n",
        "        .sort_values(by='final_amount', ascending=False)\n",
        "    )\n",
        "    result.to_csv(os.path.join(OUTPUT_DIR, 'sales_by_store.csv'), index=False)\n",
        "\n",
        "def daily_sales():\n",
        "    df = pd.read_csv(DATA_PATH)\n",
        "    df['transaction_date'] = pd.to_datetime(df['transaction_date'])\n",
        "    result = (\n",
        "        df.groupby(df['transaction_date'].dt.date)['final_amount']\n",
        "        .sum()\n",
        "        .reset_index()\n",
        "    )\n",
        "    result.to_csv(os.path.join(OUTPUT_DIR, 'daily_sales.csv'), index=False)\n",
        "\n",
        "def weekly_sales():\n",
        "    df = pd.read_csv(DATA_PATH)\n",
        "    df['transaction_date'] = pd.to_datetime(df['transaction_date'])\n",
        "    result = (\n",
        "        df.groupby(df['transaction_date'].dt.to_period('W'))['final_amount']\n",
        "        .sum()\n",
        "        .reset_index()\n",
        "    )\n",
        "    result['week'] = result['transaction_date'].astype(str)\n",
        "    result.drop(columns=['transaction_date'], inplace=True)\n",
        "    result.to_csv(os.path.join(OUTPUT_DIR, 'weekly_sales.csv'), index=False)\n",
        "\n",
        "def sales_by_aisle():\n",
        "    df = pd.read_csv(DATA_PATH)\n",
        "    result = (\n",
        "        df.groupby('aisle')['final_amount']\n",
        "        .sum()\n",
        "        .reset_index()\n",
        "        .sort_values(by='final_amount', ascending=False)\n",
        "    )\n",
        "    result.to_csv(os.path.join(OUTPUT_DIR, 'sales_by_aisle.csv'), index=False)\n",
        "\n",
        "with DAG(\n",
        "    dag_id='fmcg_pipeline',\n",
        "    start_date=datetime(2025, 1, 1),\n",
        "    schedule_interval=None,\n",
        "    catchup=False\n",
        ") as dag:\n",
        "\n",
        "    product = PythonOperator(task_id='sales_by_product', python_callable=sales_by_product)\n",
        "    store = PythonOperator(task_id='sales_by_store', python_callable=sales_by_store)\n",
        "    daily = PythonOperator(task_id='daily_sales', python_callable=daily_sales)\n",
        "    weekly = PythonOperator(task_id='weekly_sales', python_callable=weekly_sales)\n",
        "    aisle = PythonOperator(task_id='sales_by_aisle', python_callable=sales_by_aisle)\n",
        "\n",
        "    [product, store, daily, weekly, aisle]\n",
        "\"\"\"\n",
        "\n",
        "with open(dag_file_path, \"w\") as f:\n",
        "    f.write(dag_code)\n",
        "\n",
        "print(\"✅ DAG file written to:\", dag_file_path)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2O3jax4x63Eu",
        "outputId": "710627a0-8ef8-4466-ba73-438792a874ec"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "✅ DAG file written to: /root/airflow/dags/fmcg_pipeline.py\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!airflow dags list-import-errors"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Vxy0tgZPgQO-",
        "outputId": "2910acd9-1da5-4b1b-8253-3ab937ec9476"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "No data found\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pkill -f airflow || true\n",
        "!nohup airflow scheduler > ~/airflow/scheduler.log 2>&1 &\n",
        "!sleep 15\n",
        "!airflow dags list"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lhpBbpv-gTJw",
        "outputId": "87c57554-54e5-4260-95c3-8b7b910c3dc2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "^C\n",
            "\u001b[1mdag_id                      \u001b[0m\u001b[1m \u001b[0m|\u001b[1m \u001b[0m\u001b[1mfileloc                    \u001b[0m\u001b[1m \u001b[0m|\u001b[1m \u001b[0m\u001b[1mowners \u001b[0m\u001b[1m \u001b[0m|\u001b[1m \u001b[0m\u001b[1mis_paused\u001b[0m\n",
            "=============================+=============================+=========+==========\n",
            "conditional_dataset_and_time | /usr/local/lib/python3.12/d | airflow | True     \n",
            "_based_timetable             | ist-packages/airflow/exampl |         |          \n",
            "                             | e_dags/example_datasets.py  |         |          \n",
            "consume_1_and_2_with_dataset | /usr/local/lib/python3.12/d | airflow | True     \n",
            "_expressions                 | ist-packages/airflow/exampl |         |          \n",
            "                             | e_dags/example_datasets.py  |         |          \n",
            "consume_1_or_2_with_dataset_ | /usr/local/lib/python3.12/d | airflow | True     \n",
            "expressions                  | ist-packages/airflow/exampl |         |          \n",
            "                             | e_dags/example_datasets.py  |         |          \n",
            "consume_1_or_both_2_and_3_wi | /usr/local/lib/python3.12/d | airflow | True     \n",
            "th_dataset_expressions       | ist-packages/airflow/exampl |         |          \n",
            "                             | e_dags/example_datasets.py  |         |          \n",
            "dataset_consumes_1           | /usr/local/lib/python3.12/d | airflow | True     \n",
            "                             | ist-packages/airflow/exampl |         |          \n",
            "                             | e_dags/example_datasets.py  |         |          \n",
            "dataset_consumes_1_and_2     | /usr/local/lib/python3.12/d | airflow | True     \n",
            "                             | ist-packages/airflow/exampl |         |          \n",
            "                             | e_dags/example_datasets.py  |         |          \n",
            "dataset_consumes_1_never_sch | /usr/local/lib/python3.12/d | airflow | True     \n",
            "eduled                       | ist-packages/airflow/exampl |         |          \n",
            "                             | e_dags/example_datasets.py  |         |          \n",
            "dataset_consumes_unknown_nev | /usr/local/lib/python3.12/d | airflow | True     \n",
            "er_scheduled                 | ist-packages/airflow/exampl |         |          \n",
            "                             | e_dags/example_datasets.py  |         |          \n",
            "dataset_produces_1           | /usr/local/lib/python3.12/d | airflow | True     \n",
            "                             | ist-packages/airflow/exampl |         |          \n",
            "                             | e_dags/example_datasets.py  |         |          \n",
            "dataset_produces_2           | /usr/local/lib/python3.12/d | airflow | True     \n",
            "                             | ist-packages/airflow/exampl |         |          \n",
            "                             | e_dags/example_datasets.py  |         |          \n",
            "example_bash_decorator       | /usr/local/lib/python3.12/d | airflow | True     \n",
            "                             | ist-packages/airflow/exampl |         |          \n",
            "                             | e_dags/example_bash_decorat |         |          \n",
            "                             | or.py                       |         |          \n",
            "example_bash_operator        | /usr/local/lib/python3.12/d | airflow | True     \n",
            "                             | ist-packages/airflow/exampl |         |          \n",
            "                             | e_dags/example_bash_operato |         |          \n",
            "                             | r.py                        |         |          \n",
            "example_branch_datetime_oper | /usr/local/lib/python3.12/d | airflow | True     \n",
            "ator                         | ist-packages/airflow/exampl |         |          \n",
            "                             | e_dags/example_branch_datet |         |          \n",
            "                             | ime_operator.py             |         |          \n",
            "example_branch_datetime_oper | /usr/local/lib/python3.12/d | airflow | True     \n",
            "ator_2                       | ist-packages/airflow/exampl |         |          \n",
            "                             | e_dags/example_branch_datet |         |          \n",
            "                             | ime_operator.py             |         |          \n",
            "example_branch_datetime_oper | /usr/local/lib/python3.12/d | airflow | True     \n",
            "ator_3                       | ist-packages/airflow/exampl |         |          \n",
            "                             | e_dags/example_branch_datet |         |          \n",
            "                             | ime_operator.py             |         |          \n",
            "example_branch_dop_operator_ | /usr/local/lib/python3.12/d | airflow | True     \n",
            "v3                           | ist-packages/airflow/exampl |         |          \n",
            "                             | e_dags/example_branch_pytho |         |          \n",
            "                             | n_dop_operator_3.py         |         |          \n",
            "example_branch_labels        | /usr/local/lib/python3.12/d | airflow | True     \n",
            "                             | ist-packages/airflow/exampl |         |          \n",
            "                             | e_dags/example_branch_label |         |          \n",
            "                             | s.py                        |         |          \n",
            "example_complex              | /usr/local/lib/python3.12/d | airflow | True     \n",
            "                             | ist-packages/airflow/exampl |         |          \n",
            "                             | e_dags/example_complex.py   |         |          \n",
            "example_dag_decorator        | /usr/local/lib/python3.12/d | airflow | True     \n",
            "                             | ist-packages/airflow/exampl |         |          \n",
            "                             | e_dags/example_dag_decorato |         |          \n",
            "                             | r.py                        |         |          \n",
            "example_display_name         | /usr/local/lib/python3.12/d | airflow | True     \n",
            "                             | ist-packages/airflow/exampl |         |          \n",
            "                             | e_dags/example_display_name |         |          \n",
            "                             | .py                         |         |          \n",
            "example_dynamic_task_mapping | /usr/local/lib/python3.12/d | airflow | True     \n",
            "                             | ist-packages/airflow/exampl |         |          \n",
            "                             | e_dags/example_dynamic_task |         |          \n",
            "                             | _mapping.py                 |         |          \n",
            "example_dynamic_task_mapping | /usr/local/lib/python3.12/d | airflow | True     \n",
            "_with_no_taskflow_operators  | ist-packages/airflow/exampl |         |          \n",
            "                             | e_dags/example_dynamic_task |         |          \n",
            "                             | _mapping_with_no_taskflow_o |         |          \n",
            "                             | perators.py                 |         |          \n",
            "example_external_task_marker | /usr/local/lib/python3.12/d | airflow | True     \n",
            "_child                       | ist-packages/airflow/exampl |         |          \n",
            "                             | e_dags/example_external_tas |         |          \n",
            "                             | k_marker_dag.py             |         |          \n",
            "example_external_task_marker | /usr/local/lib/python3.12/d | airflow | True     \n",
            "_parent                      | ist-packages/airflow/exampl |         |          \n",
            "                             | e_dags/example_external_tas |         |          \n",
            "                             | k_marker_dag.py             |         |          \n",
            "example_nested_branch_dag    | /usr/local/lib/python3.12/d | airflow | True     \n",
            "                             | ist-packages/airflow/exampl |         |          \n",
            "                             | e_dags/example_nested_branc |         |          \n",
            "                             | h_dag.py                    |         |          \n",
            "example_params_trigger_ui    | /usr/local/lib/python3.12/d | airflow | True     \n",
            "                             | ist-packages/airflow/exampl |         |          \n",
            "                             | e_dags/example_params_trigg |         |          \n",
            "                             | er_ui.py                    |         |          \n",
            "example_params_ui_tutorial   | /usr/local/lib/python3.12/d | airflow | True     \n",
            "                             | ist-packages/airflow/exampl |         |          \n",
            "                             | e_dags/example_params_ui_tu |         |          \n",
            "                             | torial.py                   |         |          \n",
            "example_passing_params_via_t | /usr/local/lib/python3.12/d | airflow | True     \n",
            "est_command                  | ist-packages/airflow/exampl |         |          \n",
            "                             | e_dags/example_passing_para |         |          \n",
            "                             | ms_via_test_command.py      |         |          \n",
            "example_python_decorator     | /usr/local/lib/python3.12/d | airflow | True     \n",
            "                             | ist-packages/airflow/exampl |         |          \n",
            "                             | e_dags/example_python_decor |         |          \n",
            "                             | ator.py                     |         |          \n",
            "example_python_operator      | /usr/local/lib/python3.12/d | airflow | True     \n",
            "                             | ist-packages/airflow/exampl |         |          \n",
            "                             | e_dags/example_python_opera |         |          \n",
            "                             | tor.py                      |         |          \n",
            "example_sensor_decorator     | /usr/local/lib/python3.12/d | airflow | True     \n",
            "                             | ist-packages/airflow/exampl |         |          \n",
            "                             | e_dags/example_sensor_decor |         |          \n",
            "                             | ator.py                     |         |          \n",
            "example_sensors              | /usr/local/lib/python3.12/d | airflow | True     \n",
            "                             | ist-packages/airflow/exampl |         |          \n",
            "                             | e_dags/example_sensors.py   |         |          \n",
            "example_setup_teardown       | /usr/local/lib/python3.12/d | airflow | True     \n",
            "                             | ist-packages/airflow/exampl |         |          \n",
            "                             | e_dags/example_setup_teardo |         |          \n",
            "                             | wn.py                       |         |          \n",
            "example_setup_teardown_taskf | /usr/local/lib/python3.12/d | airflow | True     \n",
            "low                          | ist-packages/airflow/exampl |         |          \n",
            "                             | e_dags/example_setup_teardo |         |          \n",
            "                             | wn_taskflow.py              |         |          \n",
            "example_short_circuit_decora | /usr/local/lib/python3.12/d | airflow | True     \n",
            "tor                          | ist-packages/airflow/exampl |         |          \n",
            "                             | e_dags/example_short_circui |         |          \n",
            "                             | t_decorator.py              |         |          \n",
            "example_short_circuit_operat | /usr/local/lib/python3.12/d | airflow | True     \n",
            "or                           | ist-packages/airflow/exampl |         |          \n",
            "                             | e_dags/example_short_circui |         |          \n",
            "                             | t_operator.py               |         |          \n",
            "example_skip_dag             | /usr/local/lib/python3.12/d | airflow | True     \n",
            "                             | ist-packages/airflow/exampl |         |          \n",
            "                             | e_dags/example_skip_dag.py  |         |          \n",
            "example_sla_dag              | /usr/local/lib/python3.12/d | airflow | True     \n",
            "                             | ist-packages/airflow/exampl |         |          \n",
            "                             | e_dags/example_sla_dag.py   |         |          \n",
            "example_subdag_operator      | /usr/local/lib/python3.12/d | airflow | True     \n",
            "                             | ist-packages/airflow/exampl |         |          \n",
            "                             | e_dags/example_subdag_opera |         |          \n",
            "                             | tor.py                      |         |          \n",
            "example_subdag_operator.sect | /usr/local/lib/python3.12/d | airflow | True     \n",
            "ion-1                        | ist-packages/airflow/exampl |         |          \n",
            "                             | e_dags/example_subdag_opera |         |          \n",
            "                             | tor.py                      |         |          \n",
            "example_subdag_operator.sect | /usr/local/lib/python3.12/d | airflow | True     \n",
            "ion-2                        | ist-packages/airflow/exampl |         |          \n",
            "                             | e_dags/example_subdag_opera |         |          \n",
            "                             | tor.py                      |         |          \n",
            "example_task_group           | /usr/local/lib/python3.12/d | airflow | True     \n",
            "                             | ist-packages/airflow/exampl |         |          \n",
            "                             | e_dags/example_task_group.p |         |          \n",
            "                             | y                           |         |          \n",
            "example_task_group_decorator | /usr/local/lib/python3.12/d | airflow | True     \n",
            "                             | ist-packages/airflow/exampl |         |          \n",
            "                             | e_dags/example_task_group_d |         |          \n",
            "                             | ecorator.py                 |         |          \n",
            "example_time_delta_sensor_as | /usr/local/lib/python3.12/d | airflow | True     \n",
            "ync                          | ist-packages/airflow/exampl |         |          \n",
            "                             | e_dags/example_time_delta_s |         |          \n",
            "                             | ensor_async.py              |         |          \n",
            "example_trigger_controller_d | /usr/local/lib/python3.12/d | airflow | True     \n",
            "ag                           | ist-packages/airflow/exampl |         |          \n",
            "                             | e_dags/example_trigger_cont |         |          \n",
            "                             | roller_dag.py               |         |          \n",
            "example_trigger_target_dag   | /usr/local/lib/python3.12/d | airflow | True     \n",
            "                             | ist-packages/airflow/exampl |         |          \n",
            "                             | e_dags/example_trigger_targ |         |          \n",
            "                             | et_dag.py                   |         |          \n",
            "example_weekday_branch_opera | /usr/local/lib/python3.12/d | airflow | True     \n",
            "tor                          | ist-packages/airflow/exampl |         |          \n",
            "                             | e_dags/example_branch_day_o |         |          \n",
            "                             | f_week_operator.py          |         |          \n",
            "example_xcom                 | /usr/local/lib/python3.12/d | airflow | True     \n",
            "                             | ist-packages/airflow/exampl |         |          \n",
            "                             | e_dags/example_xcom.py      |         |          \n",
            "example_xcom_args            | /usr/local/lib/python3.12/d | airflow | True     \n",
            "                             | ist-packages/airflow/exampl |         |          \n",
            "                             | e_dags/example_xcomargs.py  |         |          \n",
            "example_xcom_args_with_opera | /usr/local/lib/python3.12/d | airflow | True     \n",
            "tors                         | ist-packages/airflow/exampl |         |          \n",
            "                             | e_dags/example_xcomargs.py  |         |          \n",
            "fmcg_pipeline                | /root/airflow/dags/fmcg_pip | airflow | True     \n",
            "                             | eline.py                    |         |          \n",
            "latest_only                  | /usr/local/lib/python3.12/d | airflow | True     \n",
            "                             | ist-packages/airflow/exampl |         |          \n",
            "                             | e_dags/example_latest_only. |         |          \n",
            "                             | py                          |         |          \n",
            "latest_only_with_trigger     | /usr/local/lib/python3.12/d | airflow | True     \n",
            "                             | ist-packages/airflow/exampl |         |          \n",
            "                             | e_dags/example_latest_only_ |         |          \n",
            "                             | with_trigger.py             |         |          \n",
            "tutorial                     | /usr/local/lib/python3.12/d | airflow | True     \n",
            "                             | ist-packages/airflow/exampl |         |          \n",
            "                             | e_dags/tutorial.py          |         |          \n",
            "tutorial_dag                 | /usr/local/lib/python3.12/d | airflow | True     \n",
            "                             | ist-packages/airflow/exampl |         |          \n",
            "                             | e_dags/tutorial_dag.py      |         |          \n",
            "tutorial_objectstorage       | /usr/local/lib/python3.12/d | airflow | True     \n",
            "                             | ist-packages/airflow/exampl |         |          \n",
            "                             | e_dags/tutorial_objectstora |         |          \n",
            "                             | ge.py                       |         |          \n",
            "tutorial_taskflow_api        | /usr/local/lib/python3.12/d | airflow | True     \n",
            "                             | ist-packages/airflow/exampl |         |          \n",
            "                             | e_dags/tutorial_taskflow_ap |         |          \n",
            "                             | i.py                        |         |          \n",
            "\u001b[2;3m                                                                                \u001b[0m\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# STEP 5: Trigger the DAG\n",
        "# ----------------------------\n",
        "!airflow dags trigger fmcg_pipeline"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DE-iCguaMnoa",
        "outputId": "181a3ff9-bf11-4fe4-f11f-ef214679127a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[\u001b[34m2026-01-02T19:11:01.568+0000\u001b[0m] {\u001b[34m__init__.py:\u001b[0m43} INFO\u001b[0m - Loaded API auth backend: \u001b[01mairflow.api.auth.backend.session\u001b[22m\u001b[0m\n",
            "\u001b[1m     \u001b[0m|\u001b[1m      \u001b[0m|\u001b[1m      \u001b[0m|\u001b[1m      \u001b[0m|\u001b[1m      \u001b[0m|\u001b[1m      \u001b[0m|\u001b[1m      \u001b[0m|\u001b[1m \u001b[0m\u001b[1mlast\u001b[0m\u001b[1m \u001b[0m|\u001b[1m     \u001b[0m|\u001b[1m      \u001b[0m|\u001b[1m     \u001b[0m|\u001b[1m      \u001b[0m\n",
            "\u001b[1m     \u001b[0m|\u001b[1m      \u001b[0m|\u001b[1m      \u001b[0m|\u001b[1m \u001b[0m\u001b[1mdata\u001b[0m\u001b[1m \u001b[0m|\u001b[1m \u001b[0m\u001b[1mdata\u001b[0m\u001b[1m \u001b[0m|\u001b[1m      \u001b[0m|\u001b[1m      \u001b[0m|\u001b[1m \u001b[0m\u001b[1m_sch\u001b[0m\u001b[1m \u001b[0m|\u001b[1m     \u001b[0m|\u001b[1m      \u001b[0m|\u001b[1m     \u001b[0m|\u001b[1m      \u001b[0m\n",
            "\u001b[1m     \u001b[0m|\u001b[1m      \u001b[0m|\u001b[1m      \u001b[0m|\u001b[1m \u001b[0m\u001b[1m_int\u001b[0m\u001b[1m \u001b[0m|\u001b[1m \u001b[0m\u001b[1m_int\u001b[0m\u001b[1m \u001b[0m|\u001b[1m      \u001b[0m|\u001b[1m \u001b[0m\u001b[1mexte\u001b[0m\u001b[1m \u001b[0m|\u001b[1m \u001b[0m\u001b[1medul\u001b[0m\u001b[1m \u001b[0m|\u001b[1m \u001b[0m\u001b[1mlog\u001b[0m\u001b[1m \u001b[0m|\u001b[1m      \u001b[0m|\u001b[1m \u001b[0m\u001b[1msta\u001b[0m\u001b[1m \u001b[0m|\u001b[1m      \u001b[0m\n",
            "\u001b[1m     \u001b[0m|\u001b[1m      \u001b[0m|\u001b[1m \u001b[0m\u001b[1mdag_\u001b[0m\u001b[1m \u001b[0m|\u001b[1m \u001b[0m\u001b[1merva\u001b[0m\u001b[1m \u001b[0m|\u001b[1m \u001b[0m\u001b[1merva\u001b[0m\u001b[1m \u001b[0m|\u001b[1m      \u001b[0m|\u001b[1m \u001b[0m\u001b[1mrnal\u001b[0m\u001b[1m \u001b[0m|\u001b[1m \u001b[0m\u001b[1ming_\u001b[0m\u001b[1m \u001b[0m|\u001b[1m \u001b[0m\u001b[1mica\u001b[0m\u001b[1m \u001b[0m|\u001b[1m      \u001b[0m|\u001b[1m \u001b[0m\u001b[1mrt_\u001b[0m\u001b[1m \u001b[0m|\u001b[1m      \u001b[0m\n",
            "\u001b[1m     \u001b[0m|\u001b[1m \u001b[0m\u001b[1mdag_\u001b[0m\u001b[1m \u001b[0m|\u001b[1m \u001b[0m\u001b[1mrun_\u001b[0m\u001b[1m \u001b[0m|\u001b[1m \u001b[0m\u001b[1ml_st\u001b[0m\u001b[1m \u001b[0m|\u001b[1m \u001b[0m\u001b[1ml_en\u001b[0m\u001b[1m \u001b[0m|\u001b[1m \u001b[0m\u001b[1mend_\u001b[0m\u001b[1m \u001b[0m|\u001b[1m \u001b[0m\u001b[1m_tri\u001b[0m\u001b[1m \u001b[0m|\u001b[1m \u001b[0m\u001b[1mdeci\u001b[0m\u001b[1m \u001b[0m|\u001b[1m \u001b[0m\u001b[1ml_d\u001b[0m\u001b[1m \u001b[0m|\u001b[1m \u001b[0m\u001b[1mrun_\u001b[0m\u001b[1m \u001b[0m|\u001b[1m \u001b[0m\u001b[1mdat\u001b[0m\u001b[1m \u001b[0m|\u001b[1m      \u001b[0m\n",
            "\u001b[1mconf\u001b[0m\u001b[1m \u001b[0m|\u001b[1m \u001b[0m\u001b[1mid  \u001b[0m\u001b[1m \u001b[0m|\u001b[1m \u001b[0m\u001b[1mid  \u001b[0m\u001b[1m \u001b[0m|\u001b[1m \u001b[0m\u001b[1mart \u001b[0m\u001b[1m \u001b[0m|\u001b[1m \u001b[0m\u001b[1md   \u001b[0m\u001b[1m \u001b[0m|\u001b[1m \u001b[0m\u001b[1mdate\u001b[0m\u001b[1m \u001b[0m|\u001b[1m \u001b[0m\u001b[1mgger\u001b[0m\u001b[1m \u001b[0m|\u001b[1m \u001b[0m\u001b[1msion\u001b[0m\u001b[1m \u001b[0m|\u001b[1m \u001b[0m\u001b[1mate\u001b[0m\u001b[1m \u001b[0m|\u001b[1m \u001b[0m\u001b[1mtype\u001b[0m\u001b[1m \u001b[0m|\u001b[1m \u001b[0m\u001b[1me  \u001b[0m\u001b[1m \u001b[0m|\u001b[1m \u001b[0m\u001b[1mstate\u001b[0m\n",
            "=====+======+======+======+======+======+======+======+=====+======+=====+======\n",
            "{}   | fmcg | manu | 2026 | 2026 | None | True | None | 202 | manu | Non | queue\n",
            "     | _pip | al__ | -01- | -01- |      |      |      | 6-0 | al   | e   | d    \n",
            "     | elin | 2026 | 02   | 02   |      |      |      | 1-0 |      |     |      \n",
            "     | e    | -01- | 19:1 | 19:1 |      |      |      | 2   |      |     |      \n",
            "     |      | 02T1 | 1:01 | 1:01 |      |      |      | 19: |      |     |      \n",
            "     |      | 9:11 | +00: | +00: |      |      |      | 11: |      |     |      \n",
            "     |      | :01+ | 00   | 00   |      |      |      | 01+ |      |     |      \n",
            "     |      | 00:0 |      |      |      |      |      | 00: |      |     |      \n",
            "     |      | 0    |      |      |      |      |      | 00  |      |     |      \n",
            "\u001b[2;3m                                                                                \u001b[0m\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!airflow tasks test fmcg_pipeline sales_by_product 2026-01-01"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Hg424pd4Sh99",
        "outputId": "24872ed3-90ce-4b8f-8034-2e1f36f0c8b9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[\u001b[34m2026-01-02T19:03:53.800+0000\u001b[0m] {\u001b[34mdagbag.py:\u001b[0m545} INFO\u001b[0m - Filling up the DagBag from \u001b[01m/root/airflow/dags\u001b[22m\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:03:54.205+0000\u001b[0m] {\u001b[34mutils.py:\u001b[0m164} INFO\u001b[0m - NumExpr defaulting to 2 threads.\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:03:54.547+0000\u001b[0m] {\u001b[34mexample_python_operator.py:\u001b[0m93} \u001b[33mWARNING\u001b[0m - \u001b[33mThe virtalenv_python example task requires virtualenv, please install it.\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:03:54.549+0000\u001b[0m] {\u001b[34mexample_local_kubernetes_executor.py:\u001b[0m40} \u001b[33mWARNING\u001b[0m - \u001b[33mCould not import DAGs in example_local_kubernetes_executor.py\u001b[0m\n",
            "\u001b[33mTraceback (most recent call last):\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/airflow/example_dags/example_local_kubernetes_executor.py\", line 38, in <module>\n",
            "    from kubernetes.client import models as k8s\n",
            "ModuleNotFoundError: No module named 'kubernetes'\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:03:54.550+0000\u001b[0m] {\u001b[34mexample_local_kubernetes_executor.py:\u001b[0m41} \u001b[33mWARNING\u001b[0m - \u001b[33mInstall Kubernetes dependencies with: pip install apache-airflow[cncf.kubernetes]\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:03:54.616+0000\u001b[0m] {\u001b[34mexample_python_decorator.py:\u001b[0m80} \u001b[33mWARNING\u001b[0m - \u001b[33mThe virtalenv_python example task requires virtualenv, please install it.\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:03:55.002+0000\u001b[0m] {\u001b[34mtutorial_taskflow_api_virtualenv.py:\u001b[0m29} \u001b[33mWARNING\u001b[0m - \u001b[33mThe tutorial_taskflow_api_virtualenv example DAG requires virtualenv, please install it.\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:03:55.263+0000\u001b[0m] {\u001b[34mexample_kubernetes_executor.py:\u001b[0m39} \u001b[33mWARNING\u001b[0m - \u001b[33mThe example_kubernetes_executor example DAG requires the kubernetes provider. Please install it with: pip install apache-airflow[cncf.kubernetes]\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:03:55.367+0000\u001b[0m] {\u001b[34mtaskinstance.py:\u001b[0m2076} INFO\u001b[0m - Dependencies all met for dep_context=\u001b[01mnon-requeueable deps\u001b[22m ti=\u001b[01m<TaskInstance: fmcg_pipeline.sales_by_product __airflow_temporary_run_2026-01-02T19:03:55.302038+00:00__ [None]>\u001b[22m\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:03:55.374+0000\u001b[0m] {\u001b[34mtaskinstance.py:\u001b[0m2076} INFO\u001b[0m - Dependencies all met for dep_context=\u001b[01mrequeueable deps\u001b[22m ti=\u001b[01m<TaskInstance: fmcg_pipeline.sales_by_product __airflow_temporary_run_2026-01-02T19:03:55.302038+00:00__ [None]>\u001b[22m\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:03:55.374+0000\u001b[0m] {\u001b[34mtaskinstance.py:\u001b[0m2306} INFO\u001b[0m - Starting attempt 1 of 1\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:03:55.375+0000\u001b[0m] {\u001b[34mtaskinstance.py:\u001b[0m2388} \u001b[33mWARNING\u001b[0m - \u001b[33mcannot record \u001b[01mqueued_duration\u001b[22m for task \u001b[01msales_by_product\u001b[22m because previous state change time has not been saved\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:03:55.376+0000\u001b[0m] {\u001b[34mtaskinstance.py:\u001b[0m2330} INFO\u001b[0m - Executing \u001b[01m<Task(PythonOperator): sales_by_product>\u001b[22m on \u001b[01m2026-01-01 00:00:00+00:00\u001b[22m\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:03:55.396+0000\u001b[0m] {\u001b[34mtaskinstance.py:\u001b[0m2648} INFO\u001b[0m - Exporting env vars: \u001b[01mAIRFLOW_CTX_DAG_OWNER='airflow' AIRFLOW_CTX_DAG_ID='fmcg_pipeline' AIRFLOW_CTX_TASK_ID='sales_by_product' AIRFLOW_CTX_EXECUTION_DATE='2026-01-01T00:00:00+00:00' AIRFLOW_CTX_TRY_NUMBER='1' AIRFLOW_CTX_DAG_RUN_ID='__airflow_temporary_run_2026-01-02T19:03:55.302038+00:00__'\u001b[22m\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:03:55.398+0000\u001b[0m] {\u001b[34mtaskinstance.py:\u001b[0m430} INFO\u001b[0m - ::endgroup::\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:03:55.460+0000\u001b[0m] {\u001b[34mpython.py:\u001b[0m237} INFO\u001b[0m - Done. Returned value was: \u001b[01mNone\u001b[22m\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:03:55.460+0000\u001b[0m] {\u001b[34mtaskinstance.py:\u001b[0m441} INFO\u001b[0m - ::group::Post task execution logs\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:03:55.461+0000\u001b[0m] {\u001b[34mtaskinstance.py:\u001b[0m1206} INFO\u001b[0m - \u001b[01m\u001b[22mMarking task as \u001b[01mSUCCESS\u001b[22m. dag_id=\u001b[01mfmcg_pipeline\u001b[22m, task_id=\u001b[01msales_by_product\u001b[22m, run_id=\u001b[01m__airflow_temporary_run_2026-01-02T19:03:55.302038+00:00__\u001b[22m, execution_date=\u001b[01m20260101T000000\u001b[22m, start_date=\u001b[01m\u001b[22m, end_date=\u001b[01m20260102T190355\u001b[22m\u001b[0m\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!airflow tasks list fmcg_pipeline"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "riOHG23NFKLm",
        "outputId": "4c00fa8d-12c9-46e6-8f5f-323de93df3cc"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "daily_sales\n",
            "sales_by_aisle\n",
            "sales_by_product\n",
            "sales_by_store\n",
            "weekly_sales\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!airflow tasks test fmcg_pipeline sales_by_product 2025-01-01"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gqj_SvsbGHkE",
        "outputId": "8e15a22b-f356-4cfb-9619-e796e4fe0c10"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[\u001b[34m2026-01-02T19:04:31.874+0000\u001b[0m] {\u001b[34mdagbag.py:\u001b[0m545} INFO\u001b[0m - Filling up the DagBag from \u001b[01m/root/airflow/dags\u001b[22m\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:04:32.422+0000\u001b[0m] {\u001b[34mutils.py:\u001b[0m164} INFO\u001b[0m - NumExpr defaulting to 2 threads.\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:04:32.758+0000\u001b[0m] {\u001b[34mexample_python_operator.py:\u001b[0m93} \u001b[33mWARNING\u001b[0m - \u001b[33mThe virtalenv_python example task requires virtualenv, please install it.\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:04:32.760+0000\u001b[0m] {\u001b[34mexample_local_kubernetes_executor.py:\u001b[0m40} \u001b[33mWARNING\u001b[0m - \u001b[33mCould not import DAGs in example_local_kubernetes_executor.py\u001b[0m\n",
            "\u001b[33mTraceback (most recent call last):\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/airflow/example_dags/example_local_kubernetes_executor.py\", line 38, in <module>\n",
            "    from kubernetes.client import models as k8s\n",
            "ModuleNotFoundError: No module named 'kubernetes'\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:04:32.761+0000\u001b[0m] {\u001b[34mexample_local_kubernetes_executor.py:\u001b[0m41} \u001b[33mWARNING\u001b[0m - \u001b[33mInstall Kubernetes dependencies with: pip install apache-airflow[cncf.kubernetes]\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:04:32.825+0000\u001b[0m] {\u001b[34mexample_python_decorator.py:\u001b[0m80} \u001b[33mWARNING\u001b[0m - \u001b[33mThe virtalenv_python example task requires virtualenv, please install it.\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:04:33.383+0000\u001b[0m] {\u001b[34mtutorial_taskflow_api_virtualenv.py:\u001b[0m29} \u001b[33mWARNING\u001b[0m - \u001b[33mThe tutorial_taskflow_api_virtualenv example DAG requires virtualenv, please install it.\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:04:33.699+0000\u001b[0m] {\u001b[34mexample_kubernetes_executor.py:\u001b[0m39} \u001b[33mWARNING\u001b[0m - \u001b[33mThe example_kubernetes_executor example DAG requires the kubernetes provider. Please install it with: pip install apache-airflow[cncf.kubernetes]\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:04:33.885+0000\u001b[0m] {\u001b[34mtaskinstance.py:\u001b[0m2076} INFO\u001b[0m - Dependencies all met for dep_context=\u001b[01mnon-requeueable deps\u001b[22m ti=\u001b[01m<TaskInstance: fmcg_pipeline.sales_by_product __airflow_temporary_run_2026-01-02T19:04:33.787057+00:00__ [None]>\u001b[22m\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:04:33.905+0000\u001b[0m] {\u001b[34mtaskinstance.py:\u001b[0m2076} INFO\u001b[0m - Dependencies all met for dep_context=\u001b[01mrequeueable deps\u001b[22m ti=\u001b[01m<TaskInstance: fmcg_pipeline.sales_by_product __airflow_temporary_run_2026-01-02T19:04:33.787057+00:00__ [None]>\u001b[22m\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:04:33.908+0000\u001b[0m] {\u001b[34mtaskinstance.py:\u001b[0m2306} INFO\u001b[0m - Starting attempt 1 of 1\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:04:33.908+0000\u001b[0m] {\u001b[34mtaskinstance.py:\u001b[0m2388} \u001b[33mWARNING\u001b[0m - \u001b[33mcannot record \u001b[01mqueued_duration\u001b[22m for task \u001b[01msales_by_product\u001b[22m because previous state change time has not been saved\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:04:33.909+0000\u001b[0m] {\u001b[34mtaskinstance.py:\u001b[0m2330} INFO\u001b[0m - Executing \u001b[01m<Task(PythonOperator): sales_by_product>\u001b[22m on \u001b[01m2025-01-01 00:00:00+00:00\u001b[22m\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:04:33.938+0000\u001b[0m] {\u001b[34mtaskinstance.py:\u001b[0m2648} INFO\u001b[0m - Exporting env vars: \u001b[01mAIRFLOW_CTX_DAG_OWNER='airflow' AIRFLOW_CTX_DAG_ID='fmcg_pipeline' AIRFLOW_CTX_TASK_ID='sales_by_product' AIRFLOW_CTX_EXECUTION_DATE='2025-01-01T00:00:00+00:00' AIRFLOW_CTX_TRY_NUMBER='1' AIRFLOW_CTX_DAG_RUN_ID='__airflow_temporary_run_2026-01-02T19:04:33.787057+00:00__'\u001b[22m\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:04:33.943+0000\u001b[0m] {\u001b[34mtaskinstance.py:\u001b[0m430} INFO\u001b[0m - ::endgroup::\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:04:33.960+0000\u001b[0m] {\u001b[34mpython.py:\u001b[0m237} INFO\u001b[0m - Done. Returned value was: \u001b[01mNone\u001b[22m\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:04:33.960+0000\u001b[0m] {\u001b[34mtaskinstance.py:\u001b[0m441} INFO\u001b[0m - ::group::Post task execution logs\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:04:33.961+0000\u001b[0m] {\u001b[34mtaskinstance.py:\u001b[0m1206} INFO\u001b[0m - \u001b[01m\u001b[22mMarking task as \u001b[01mSUCCESS\u001b[22m. dag_id=\u001b[01mfmcg_pipeline\u001b[22m, task_id=\u001b[01msales_by_product\u001b[22m, run_id=\u001b[01m__airflow_temporary_run_2026-01-02T19:04:33.787057+00:00__\u001b[22m, execution_date=\u001b[01m20250101T000000\u001b[22m, start_date=\u001b[01m\u001b[22m, end_date=\u001b[01m20260102T190433\u001b[22m\u001b[0m\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!airflow tasks test fmcg_pipeline daily_sales 2025-01-01"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "j8KLUq9PGOpF",
        "outputId": "9ed4bfc6-db08-4280-a7b9-0f0e525eea12"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[\u001b[34m2026-01-02T19:05:04.456+0000\u001b[0m] {\u001b[34mdagbag.py:\u001b[0m545} INFO\u001b[0m - Filling up the DagBag from \u001b[01m/root/airflow/dags\u001b[22m\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:05:04.731+0000\u001b[0m] {\u001b[34mutils.py:\u001b[0m164} INFO\u001b[0m - NumExpr defaulting to 2 threads.\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:05:04.952+0000\u001b[0m] {\u001b[34mexample_python_operator.py:\u001b[0m93} \u001b[33mWARNING\u001b[0m - \u001b[33mThe virtalenv_python example task requires virtualenv, please install it.\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:05:04.955+0000\u001b[0m] {\u001b[34mexample_local_kubernetes_executor.py:\u001b[0m40} \u001b[33mWARNING\u001b[0m - \u001b[33mCould not import DAGs in example_local_kubernetes_executor.py\u001b[0m\n",
            "\u001b[33mTraceback (most recent call last):\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/airflow/example_dags/example_local_kubernetes_executor.py\", line 38, in <module>\n",
            "    from kubernetes.client import models as k8s\n",
            "ModuleNotFoundError: No module named 'kubernetes'\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:05:04.956+0000\u001b[0m] {\u001b[34mexample_local_kubernetes_executor.py:\u001b[0m41} \u001b[33mWARNING\u001b[0m - \u001b[33mInstall Kubernetes dependencies with: pip install apache-airflow[cncf.kubernetes]\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:05:05.018+0000\u001b[0m] {\u001b[34mexample_python_decorator.py:\u001b[0m80} \u001b[33mWARNING\u001b[0m - \u001b[33mThe virtalenv_python example task requires virtualenv, please install it.\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:05:05.448+0000\u001b[0m] {\u001b[34mtutorial_taskflow_api_virtualenv.py:\u001b[0m29} \u001b[33mWARNING\u001b[0m - \u001b[33mThe tutorial_taskflow_api_virtualenv example DAG requires virtualenv, please install it.\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:05:05.698+0000\u001b[0m] {\u001b[34mexample_kubernetes_executor.py:\u001b[0m39} \u001b[33mWARNING\u001b[0m - \u001b[33mThe example_kubernetes_executor example DAG requires the kubernetes provider. Please install it with: pip install apache-airflow[cncf.kubernetes]\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:05:05.778+0000\u001b[0m] {\u001b[34mtaskinstance.py:\u001b[0m2076} INFO\u001b[0m - Dependencies all met for dep_context=\u001b[01mnon-requeueable deps\u001b[22m ti=\u001b[01m<TaskInstance: fmcg_pipeline.daily_sales __airflow_temporary_run_2026-01-02T19:05:05.728344+00:00__ [None]>\u001b[22m\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:05:05.784+0000\u001b[0m] {\u001b[34mtaskinstance.py:\u001b[0m2076} INFO\u001b[0m - Dependencies all met for dep_context=\u001b[01mrequeueable deps\u001b[22m ti=\u001b[01m<TaskInstance: fmcg_pipeline.daily_sales __airflow_temporary_run_2026-01-02T19:05:05.728344+00:00__ [None]>\u001b[22m\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:05:05.785+0000\u001b[0m] {\u001b[34mtaskinstance.py:\u001b[0m2306} INFO\u001b[0m - Starting attempt 1 of 1\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:05:05.785+0000\u001b[0m] {\u001b[34mtaskinstance.py:\u001b[0m2388} \u001b[33mWARNING\u001b[0m - \u001b[33mcannot record \u001b[01mqueued_duration\u001b[22m for task \u001b[01mdaily_sales\u001b[22m because previous state change time has not been saved\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:05:05.786+0000\u001b[0m] {\u001b[34mtaskinstance.py:\u001b[0m2330} INFO\u001b[0m - Executing \u001b[01m<Task(PythonOperator): daily_sales>\u001b[22m on \u001b[01m2025-01-01 00:00:00+00:00\u001b[22m\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:05:05.802+0000\u001b[0m] {\u001b[34mtaskinstance.py:\u001b[0m2648} INFO\u001b[0m - Exporting env vars: \u001b[01mAIRFLOW_CTX_DAG_OWNER='airflow' AIRFLOW_CTX_DAG_ID='fmcg_pipeline' AIRFLOW_CTX_TASK_ID='daily_sales' AIRFLOW_CTX_EXECUTION_DATE='2025-01-01T00:00:00+00:00' AIRFLOW_CTX_TRY_NUMBER='1' AIRFLOW_CTX_DAG_RUN_ID='__airflow_temporary_run_2026-01-02T19:05:05.728344+00:00__'\u001b[22m\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:05:05.804+0000\u001b[0m] {\u001b[34mtaskinstance.py:\u001b[0m430} INFO\u001b[0m - ::endgroup::\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:05:05.822+0000\u001b[0m] {\u001b[34mpython.py:\u001b[0m237} INFO\u001b[0m - Done. Returned value was: \u001b[01mNone\u001b[22m\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:05:05.823+0000\u001b[0m] {\u001b[34mtaskinstance.py:\u001b[0m441} INFO\u001b[0m - ::group::Post task execution logs\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:05:05.823+0000\u001b[0m] {\u001b[34mtaskinstance.py:\u001b[0m1206} INFO\u001b[0m - \u001b[01m\u001b[22mMarking task as \u001b[01mSUCCESS\u001b[22m. dag_id=\u001b[01mfmcg_pipeline\u001b[22m, task_id=\u001b[01mdaily_sales\u001b[22m, run_id=\u001b[01m__airflow_temporary_run_2026-01-02T19:05:05.728344+00:00__\u001b[22m, execution_date=\u001b[01m20250101T000000\u001b[22m, start_date=\u001b[01m\u001b[22m, end_date=\u001b[01m20260102T190505\u001b[22m\u001b[0m\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!airflow tasks test fmcg_pipeline sales_by_aisle 2025-01-01"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mkiQV7MTGWnq",
        "outputId": "0827e0f0-a2bd-4b22-b804-1c88b85f97cb"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[\u001b[34m2026-01-02T19:05:47.207+0000\u001b[0m] {\u001b[34mdagbag.py:\u001b[0m545} INFO\u001b[0m - Filling up the DagBag from \u001b[01m/root/airflow/dags\u001b[22m\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:05:47.566+0000\u001b[0m] {\u001b[34mutils.py:\u001b[0m164} INFO\u001b[0m - NumExpr defaulting to 2 threads.\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:05:47.787+0000\u001b[0m] {\u001b[34mexample_python_operator.py:\u001b[0m93} \u001b[33mWARNING\u001b[0m - \u001b[33mThe virtalenv_python example task requires virtualenv, please install it.\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:05:47.788+0000\u001b[0m] {\u001b[34mexample_local_kubernetes_executor.py:\u001b[0m40} \u001b[33mWARNING\u001b[0m - \u001b[33mCould not import DAGs in example_local_kubernetes_executor.py\u001b[0m\n",
            "\u001b[33mTraceback (most recent call last):\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/airflow/example_dags/example_local_kubernetes_executor.py\", line 38, in <module>\n",
            "    from kubernetes.client import models as k8s\n",
            "ModuleNotFoundError: No module named 'kubernetes'\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:05:47.789+0000\u001b[0m] {\u001b[34mexample_local_kubernetes_executor.py:\u001b[0m41} \u001b[33mWARNING\u001b[0m - \u001b[33mInstall Kubernetes dependencies with: pip install apache-airflow[cncf.kubernetes]\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:05:47.832+0000\u001b[0m] {\u001b[34mexample_python_decorator.py:\u001b[0m80} \u001b[33mWARNING\u001b[0m - \u001b[33mThe virtalenv_python example task requires virtualenv, please install it.\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:05:48.205+0000\u001b[0m] {\u001b[34mtutorial_taskflow_api_virtualenv.py:\u001b[0m29} \u001b[33mWARNING\u001b[0m - \u001b[33mThe tutorial_taskflow_api_virtualenv example DAG requires virtualenv, please install it.\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:05:48.386+0000\u001b[0m] {\u001b[34mexample_kubernetes_executor.py:\u001b[0m39} \u001b[33mWARNING\u001b[0m - \u001b[33mThe example_kubernetes_executor example DAG requires the kubernetes provider. Please install it with: pip install apache-airflow[cncf.kubernetes]\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:05:48.475+0000\u001b[0m] {\u001b[34mtaskinstance.py:\u001b[0m2076} INFO\u001b[0m - Dependencies all met for dep_context=\u001b[01mnon-requeueable deps\u001b[22m ti=\u001b[01m<TaskInstance: fmcg_pipeline.sales_by_aisle __airflow_temporary_run_2026-01-02T19:05:48.415934+00:00__ [None]>\u001b[22m\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:05:48.483+0000\u001b[0m] {\u001b[34mtaskinstance.py:\u001b[0m2076} INFO\u001b[0m - Dependencies all met for dep_context=\u001b[01mrequeueable deps\u001b[22m ti=\u001b[01m<TaskInstance: fmcg_pipeline.sales_by_aisle __airflow_temporary_run_2026-01-02T19:05:48.415934+00:00__ [None]>\u001b[22m\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:05:48.484+0000\u001b[0m] {\u001b[34mtaskinstance.py:\u001b[0m2306} INFO\u001b[0m - Starting attempt 1 of 1\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:05:48.484+0000\u001b[0m] {\u001b[34mtaskinstance.py:\u001b[0m2388} \u001b[33mWARNING\u001b[0m - \u001b[33mcannot record \u001b[01mqueued_duration\u001b[22m for task \u001b[01msales_by_aisle\u001b[22m because previous state change time has not been saved\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:05:48.485+0000\u001b[0m] {\u001b[34mtaskinstance.py:\u001b[0m2330} INFO\u001b[0m - Executing \u001b[01m<Task(PythonOperator): sales_by_aisle>\u001b[22m on \u001b[01m2025-01-01 00:00:00+00:00\u001b[22m\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:05:48.510+0000\u001b[0m] {\u001b[34mtaskinstance.py:\u001b[0m2648} INFO\u001b[0m - Exporting env vars: \u001b[01mAIRFLOW_CTX_DAG_OWNER='airflow' AIRFLOW_CTX_DAG_ID='fmcg_pipeline' AIRFLOW_CTX_TASK_ID='sales_by_aisle' AIRFLOW_CTX_EXECUTION_DATE='2025-01-01T00:00:00+00:00' AIRFLOW_CTX_TRY_NUMBER='1' AIRFLOW_CTX_DAG_RUN_ID='__airflow_temporary_run_2026-01-02T19:05:48.415934+00:00__'\u001b[22m\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:05:48.512+0000\u001b[0m] {\u001b[34mtaskinstance.py:\u001b[0m430} INFO\u001b[0m - ::endgroup::\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:05:48.524+0000\u001b[0m] {\u001b[34mpython.py:\u001b[0m237} INFO\u001b[0m - Done. Returned value was: \u001b[01mNone\u001b[22m\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:05:48.524+0000\u001b[0m] {\u001b[34mtaskinstance.py:\u001b[0m441} INFO\u001b[0m - ::group::Post task execution logs\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:05:48.525+0000\u001b[0m] {\u001b[34mtaskinstance.py:\u001b[0m1206} INFO\u001b[0m - \u001b[01m\u001b[22mMarking task as \u001b[01mSUCCESS\u001b[22m. dag_id=\u001b[01mfmcg_pipeline\u001b[22m, task_id=\u001b[01msales_by_aisle\u001b[22m, run_id=\u001b[01m__airflow_temporary_run_2026-01-02T19:05:48.415934+00:00__\u001b[22m, execution_date=\u001b[01m20250101T000000\u001b[22m, start_date=\u001b[01m\u001b[22m, end_date=\u001b[01m20260102T190548\u001b[22m\u001b[0m\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!airflow tasks test fmcg_pipeline sales_by_store 2025-01-01"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mqqAM7TkGgvf",
        "outputId": "0d221f51-e018-45e1-c20a-d3f2fc72eb13"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[\u001b[34m2026-01-02T19:11:23.934+0000\u001b[0m] {\u001b[34mdagbag.py:\u001b[0m545} INFO\u001b[0m - Filling up the DagBag from \u001b[01m/root/airflow/dags\u001b[22m\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:11:24.204+0000\u001b[0m] {\u001b[34mutils.py:\u001b[0m164} INFO\u001b[0m - NumExpr defaulting to 2 threads.\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:11:24.427+0000\u001b[0m] {\u001b[34mexample_python_operator.py:\u001b[0m93} \u001b[33mWARNING\u001b[0m - \u001b[33mThe virtalenv_python example task requires virtualenv, please install it.\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:11:24.429+0000\u001b[0m] {\u001b[34mexample_local_kubernetes_executor.py:\u001b[0m40} \u001b[33mWARNING\u001b[0m - \u001b[33mCould not import DAGs in example_local_kubernetes_executor.py\u001b[0m\n",
            "\u001b[33mTraceback (most recent call last):\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/airflow/example_dags/example_local_kubernetes_executor.py\", line 38, in <module>\n",
            "    from kubernetes.client import models as k8s\n",
            "ModuleNotFoundError: No module named 'kubernetes'\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:11:24.430+0000\u001b[0m] {\u001b[34mexample_local_kubernetes_executor.py:\u001b[0m41} \u001b[33mWARNING\u001b[0m - \u001b[33mInstall Kubernetes dependencies with: pip install apache-airflow[cncf.kubernetes]\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:11:24.471+0000\u001b[0m] {\u001b[34mexample_python_decorator.py:\u001b[0m80} \u001b[33mWARNING\u001b[0m - \u001b[33mThe virtalenv_python example task requires virtualenv, please install it.\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:11:25.008+0000\u001b[0m] {\u001b[34mtutorial_taskflow_api_virtualenv.py:\u001b[0m29} \u001b[33mWARNING\u001b[0m - \u001b[33mThe tutorial_taskflow_api_virtualenv example DAG requires virtualenv, please install it.\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:11:25.280+0000\u001b[0m] {\u001b[34mexample_kubernetes_executor.py:\u001b[0m39} \u001b[33mWARNING\u001b[0m - \u001b[33mThe example_kubernetes_executor example DAG requires the kubernetes provider. Please install it with: pip install apache-airflow[cncf.kubernetes]\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:11:25.396+0000\u001b[0m] {\u001b[34mtaskinstance.py:\u001b[0m2076} INFO\u001b[0m - Dependencies all met for dep_context=\u001b[01mnon-requeueable deps\u001b[22m ti=\u001b[01m<TaskInstance: fmcg_pipeline.sales_by_store __airflow_temporary_run_2026-01-02T19:11:25.321428+00:00__ [None]>\u001b[22m\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:11:25.404+0000\u001b[0m] {\u001b[34mtaskinstance.py:\u001b[0m2076} INFO\u001b[0m - Dependencies all met for dep_context=\u001b[01mrequeueable deps\u001b[22m ti=\u001b[01m<TaskInstance: fmcg_pipeline.sales_by_store __airflow_temporary_run_2026-01-02T19:11:25.321428+00:00__ [None]>\u001b[22m\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:11:25.404+0000\u001b[0m] {\u001b[34mtaskinstance.py:\u001b[0m2306} INFO\u001b[0m - Starting attempt 1 of 1\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:11:25.405+0000\u001b[0m] {\u001b[34mtaskinstance.py:\u001b[0m2388} \u001b[33mWARNING\u001b[0m - \u001b[33mcannot record \u001b[01mqueued_duration\u001b[22m for task \u001b[01msales_by_store\u001b[22m because previous state change time has not been saved\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:11:25.406+0000\u001b[0m] {\u001b[34mtaskinstance.py:\u001b[0m2330} INFO\u001b[0m - Executing \u001b[01m<Task(PythonOperator): sales_by_store>\u001b[22m on \u001b[01m2025-01-01 00:00:00+00:00\u001b[22m\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:11:25.428+0000\u001b[0m] {\u001b[34mtaskinstance.py:\u001b[0m2648} INFO\u001b[0m - Exporting env vars: \u001b[01mAIRFLOW_CTX_DAG_OWNER='airflow' AIRFLOW_CTX_DAG_ID='fmcg_pipeline' AIRFLOW_CTX_TASK_ID='sales_by_store' AIRFLOW_CTX_EXECUTION_DATE='2025-01-01T00:00:00+00:00' AIRFLOW_CTX_TRY_NUMBER='1' AIRFLOW_CTX_DAG_RUN_ID='__airflow_temporary_run_2026-01-02T19:11:25.321428+00:00__'\u001b[22m\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:11:25.433+0000\u001b[0m] {\u001b[34mtaskinstance.py:\u001b[0m430} INFO\u001b[0m - ::endgroup::\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:11:25.450+0000\u001b[0m] {\u001b[34mpython.py:\u001b[0m237} INFO\u001b[0m - Done. Returned value was: \u001b[01mNone\u001b[22m\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:11:25.450+0000\u001b[0m] {\u001b[34mtaskinstance.py:\u001b[0m441} INFO\u001b[0m - ::group::Post task execution logs\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:11:25.451+0000\u001b[0m] {\u001b[34mtaskinstance.py:\u001b[0m1206} INFO\u001b[0m - \u001b[01m\u001b[22mMarking task as \u001b[01mSUCCESS\u001b[22m. dag_id=\u001b[01mfmcg_pipeline\u001b[22m, task_id=\u001b[01msales_by_store\u001b[22m, run_id=\u001b[01m__airflow_temporary_run_2026-01-02T19:11:25.321428+00:00__\u001b[22m, execution_date=\u001b[01m20250101T000000\u001b[22m, start_date=\u001b[01m\u001b[22m, end_date=\u001b[01m20260102T191125\u001b[22m\u001b[0m\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!airflow tasks test fmcg_pipeline weekly_sales 2025-01-01"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Ee70kPP8Gk6c",
        "outputId": "d060fb9b-1746-4234-e825-7cde3cf477f4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[\u001b[34m2026-01-02T19:07:01.358+0000\u001b[0m] {\u001b[34mdagbag.py:\u001b[0m545} INFO\u001b[0m - Filling up the DagBag from \u001b[01m/root/airflow/dags\u001b[22m\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:07:01.628+0000\u001b[0m] {\u001b[34mutils.py:\u001b[0m164} INFO\u001b[0m - NumExpr defaulting to 2 threads.\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:07:01.853+0000\u001b[0m] {\u001b[34mexample_python_operator.py:\u001b[0m93} \u001b[33mWARNING\u001b[0m - \u001b[33mThe virtalenv_python example task requires virtualenv, please install it.\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:07:01.855+0000\u001b[0m] {\u001b[34mexample_local_kubernetes_executor.py:\u001b[0m40} \u001b[33mWARNING\u001b[0m - \u001b[33mCould not import DAGs in example_local_kubernetes_executor.py\u001b[0m\n",
            "\u001b[33mTraceback (most recent call last):\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/airflow/example_dags/example_local_kubernetes_executor.py\", line 38, in <module>\n",
            "    from kubernetes.client import models as k8s\n",
            "ModuleNotFoundError: No module named 'kubernetes'\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:07:01.856+0000\u001b[0m] {\u001b[34mexample_local_kubernetes_executor.py:\u001b[0m41} \u001b[33mWARNING\u001b[0m - \u001b[33mInstall Kubernetes dependencies with: pip install apache-airflow[cncf.kubernetes]\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:07:01.906+0000\u001b[0m] {\u001b[34mexample_python_decorator.py:\u001b[0m80} \u001b[33mWARNING\u001b[0m - \u001b[33mThe virtalenv_python example task requires virtualenv, please install it.\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:07:02.414+0000\u001b[0m] {\u001b[34mtutorial_taskflow_api_virtualenv.py:\u001b[0m29} \u001b[33mWARNING\u001b[0m - \u001b[33mThe tutorial_taskflow_api_virtualenv example DAG requires virtualenv, please install it.\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:07:02.678+0000\u001b[0m] {\u001b[34mexample_kubernetes_executor.py:\u001b[0m39} \u001b[33mWARNING\u001b[0m - \u001b[33mThe example_kubernetes_executor example DAG requires the kubernetes provider. Please install it with: pip install apache-airflow[cncf.kubernetes]\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:07:02.793+0000\u001b[0m] {\u001b[34mtaskinstance.py:\u001b[0m2076} INFO\u001b[0m - Dependencies all met for dep_context=\u001b[01mnon-requeueable deps\u001b[22m ti=\u001b[01m<TaskInstance: fmcg_pipeline.weekly_sales __airflow_temporary_run_2026-01-02T19:07:02.724628+00:00__ [None]>\u001b[22m\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:07:02.801+0000\u001b[0m] {\u001b[34mtaskinstance.py:\u001b[0m2076} INFO\u001b[0m - Dependencies all met for dep_context=\u001b[01mrequeueable deps\u001b[22m ti=\u001b[01m<TaskInstance: fmcg_pipeline.weekly_sales __airflow_temporary_run_2026-01-02T19:07:02.724628+00:00__ [None]>\u001b[22m\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:07:02.802+0000\u001b[0m] {\u001b[34mtaskinstance.py:\u001b[0m2306} INFO\u001b[0m - Starting attempt 1 of 1\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:07:02.802+0000\u001b[0m] {\u001b[34mtaskinstance.py:\u001b[0m2388} \u001b[33mWARNING\u001b[0m - \u001b[33mcannot record \u001b[01mqueued_duration\u001b[22m for task \u001b[01mweekly_sales\u001b[22m because previous state change time has not been saved\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:07:02.803+0000\u001b[0m] {\u001b[34mtaskinstance.py:\u001b[0m2330} INFO\u001b[0m - Executing \u001b[01m<Task(PythonOperator): weekly_sales>\u001b[22m on \u001b[01m2025-01-01 00:00:00+00:00\u001b[22m\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:07:02.826+0000\u001b[0m] {\u001b[34mtaskinstance.py:\u001b[0m2648} INFO\u001b[0m - Exporting env vars: \u001b[01mAIRFLOW_CTX_DAG_OWNER='airflow' AIRFLOW_CTX_DAG_ID='fmcg_pipeline' AIRFLOW_CTX_TASK_ID='weekly_sales' AIRFLOW_CTX_EXECUTION_DATE='2025-01-01T00:00:00+00:00' AIRFLOW_CTX_TRY_NUMBER='1' AIRFLOW_CTX_DAG_RUN_ID='__airflow_temporary_run_2026-01-02T19:07:02.724628+00:00__'\u001b[22m\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:07:02.829+0000\u001b[0m] {\u001b[34mtaskinstance.py:\u001b[0m430} INFO\u001b[0m - ::endgroup::\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:07:02.858+0000\u001b[0m] {\u001b[34mpython.py:\u001b[0m237} INFO\u001b[0m - Done. Returned value was: \u001b[01mNone\u001b[22m\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:07:02.858+0000\u001b[0m] {\u001b[34mtaskinstance.py:\u001b[0m441} INFO\u001b[0m - ::group::Post task execution logs\u001b[0m\n",
            "[\u001b[34m2026-01-02T19:07:02.859+0000\u001b[0m] {\u001b[34mtaskinstance.py:\u001b[0m1206} INFO\u001b[0m - \u001b[01m\u001b[22mMarking task as \u001b[01mSUCCESS\u001b[22m. dag_id=\u001b[01mfmcg_pipeline\u001b[22m, task_id=\u001b[01mweekly_sales\u001b[22m, run_id=\u001b[01m__airflow_temporary_run_2026-01-02T19:07:02.724628+00:00__\u001b[22m, execution_date=\u001b[01m20250101T000000\u001b[22m, start_date=\u001b[01m\u001b[22m, end_date=\u001b[01m20260102T190702\u001b[22m\u001b[0m\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!ls ~/airflow/data/"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gUaAvburHFVu",
        "outputId": "da062bd2-953c-4606-8f9b-79b22a235e80"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "'cleaned&transformed_fmcg_data.csv'   sales_by_aisle.csv     weekly_sales.csv\n",
            " daily_sales.csv\t\t      sales_by_product.csv\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import files\n",
        "\n",
        "csv_files = [\n",
        "    \"sales_by_store.csv\",\n",
        "    \"sales_by_product.csv\",\n",
        "    \"daily_sales.csv\",\n",
        "    \"weekly_sales.csv\",\n",
        "    \"sales_by_aisle.csv\"\n",
        "]\n",
        "\n",
        "for file in csv_files:\n",
        "    files.download(f\"/root/airflow/data/{file}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 17
        },
        "id": "H9IFnOpCHL46",
        "outputId": "8ed2536a-9ddc-4cf1-b5d4-e283d2077345"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ],
            "application/javascript": [
              "\n",
              "    async function download(id, filename, size) {\n",
              "      if (!google.colab.kernel.accessAllowed) {\n",
              "        return;\n",
              "      }\n",
              "      const div = document.createElement('div');\n",
              "      const label = document.createElement('label');\n",
              "      label.textContent = `Downloading \"${filename}\": `;\n",
              "      div.appendChild(label);\n",
              "      const progress = document.createElement('progress');\n",
              "      progress.max = size;\n",
              "      div.appendChild(progress);\n",
              "      document.body.appendChild(div);\n",
              "\n",
              "      const buffers = [];\n",
              "      let downloaded = 0;\n",
              "\n",
              "      const channel = await google.colab.kernel.comms.open(id);\n",
              "      // Send a message to notify the kernel that we're ready.\n",
              "      channel.send({})\n",
              "\n",
              "      for await (const message of channel.messages) {\n",
              "        // Send a message to notify the kernel that we're ready.\n",
              "        channel.send({})\n",
              "        if (message.buffers) {\n",
              "          for (const buffer of message.buffers) {\n",
              "            buffers.push(buffer);\n",
              "            downloaded += buffer.byteLength;\n",
              "            progress.value = downloaded;\n",
              "          }\n",
              "        }\n",
              "      }\n",
              "      const blob = new Blob(buffers, {type: 'application/binary'});\n",
              "      const a = document.createElement('a');\n",
              "      a.href = window.URL.createObjectURL(blob);\n",
              "      a.download = filename;\n",
              "      div.appendChild(a);\n",
              "      a.click();\n",
              "      div.remove();\n",
              "    }\n",
              "  "
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ],
            "application/javascript": [
              "download(\"download_83b45b61-1cf5-46ff-b434-4e205dca9de8\", \"sales_by_product.csv\", 323)"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ],
            "application/javascript": [
              "\n",
              "    async function download(id, filename, size) {\n",
              "      if (!google.colab.kernel.accessAllowed) {\n",
              "        return;\n",
              "      }\n",
              "      const div = document.createElement('div');\n",
              "      const label = document.createElement('label');\n",
              "      label.textContent = `Downloading \"${filename}\": `;\n",
              "      div.appendChild(label);\n",
              "      const progress = document.createElement('progress');\n",
              "      progress.max = size;\n",
              "      div.appendChild(progress);\n",
              "      document.body.appendChild(div);\n",
              "\n",
              "      const buffers = [];\n",
              "      let downloaded = 0;\n",
              "\n",
              "      const channel = await google.colab.kernel.comms.open(id);\n",
              "      // Send a message to notify the kernel that we're ready.\n",
              "      channel.send({})\n",
              "\n",
              "      for await (const message of channel.messages) {\n",
              "        // Send a message to notify the kernel that we're ready.\n",
              "        channel.send({})\n",
              "        if (message.buffers) {\n",
              "          for (const buffer of message.buffers) {\n",
              "            buffers.push(buffer);\n",
              "            downloaded += buffer.byteLength;\n",
              "            progress.value = downloaded;\n",
              "          }\n",
              "        }\n",
              "      }\n",
              "      const blob = new Blob(buffers, {type: 'application/binary'});\n",
              "      const a = document.createElement('a');\n",
              "      a.href = window.URL.createObjectURL(blob);\n",
              "      a.download = filename;\n",
              "      div.appendChild(a);\n",
              "      a.click();\n",
              "      div.remove();\n",
              "    }\n",
              "  "
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ],
            "application/javascript": [
              "download(\"download_c1382065-3c22-4798-aae9-d1bddf8d3ddd\", \"daily_sales.csv\", 13263)"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ],
            "application/javascript": [
              "\n",
              "    async function download(id, filename, size) {\n",
              "      if (!google.colab.kernel.accessAllowed) {\n",
              "        return;\n",
              "      }\n",
              "      const div = document.createElement('div');\n",
              "      const label = document.createElement('label');\n",
              "      label.textContent = `Downloading \"${filename}\": `;\n",
              "      div.appendChild(label);\n",
              "      const progress = document.createElement('progress');\n",
              "      progress.max = size;\n",
              "      div.appendChild(progress);\n",
              "      document.body.appendChild(div);\n",
              "\n",
              "      const buffers = [];\n",
              "      let downloaded = 0;\n",
              "\n",
              "      const channel = await google.colab.kernel.comms.open(id);\n",
              "      // Send a message to notify the kernel that we're ready.\n",
              "      channel.send({})\n",
              "\n",
              "      for await (const message of channel.messages) {\n",
              "        // Send a message to notify the kernel that we're ready.\n",
              "        channel.send({})\n",
              "        if (message.buffers) {\n",
              "          for (const buffer of message.buffers) {\n",
              "            buffers.push(buffer);\n",
              "            downloaded += buffer.byteLength;\n",
              "            progress.value = downloaded;\n",
              "          }\n",
              "        }\n",
              "      }\n",
              "      const blob = new Blob(buffers, {type: 'application/binary'});\n",
              "      const a = document.createElement('a');\n",
              "      a.href = window.URL.createObjectURL(blob);\n",
              "      a.download = filename;\n",
              "      div.appendChild(a);\n",
              "      a.click();\n",
              "      div.remove();\n",
              "    }\n",
              "  "
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ],
            "application/javascript": [
              "download(\"download_21879945-77d8-4023-8dea-81227abab895\", \"weekly_sales.csv\", 3134)"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ],
            "application/javascript": [
              "\n",
              "    async function download(id, filename, size) {\n",
              "      if (!google.colab.kernel.accessAllowed) {\n",
              "        return;\n",
              "      }\n",
              "      const div = document.createElement('div');\n",
              "      const label = document.createElement('label');\n",
              "      label.textContent = `Downloading \"${filename}\": `;\n",
              "      div.appendChild(label);\n",
              "      const progress = document.createElement('progress');\n",
              "      progress.max = size;\n",
              "      div.appendChild(progress);\n",
              "      document.body.appendChild(div);\n",
              "\n",
              "      const buffers = [];\n",
              "      let downloaded = 0;\n",
              "\n",
              "      const channel = await google.colab.kernel.comms.open(id);\n",
              "      // Send a message to notify the kernel that we're ready.\n",
              "      channel.send({})\n",
              "\n",
              "      for await (const message of channel.messages) {\n",
              "        // Send a message to notify the kernel that we're ready.\n",
              "        channel.send({})\n",
              "        if (message.buffers) {\n",
              "          for (const buffer of message.buffers) {\n",
              "            buffers.push(buffer);\n",
              "            downloaded += buffer.byteLength;\n",
              "            progress.value = downloaded;\n",
              "          }\n",
              "        }\n",
              "      }\n",
              "      const blob = new Blob(buffers, {type: 'application/binary'});\n",
              "      const a = document.createElement('a');\n",
              "      a.href = window.URL.createObjectURL(blob);\n",
              "      a.download = filename;\n",
              "      div.appendChild(a);\n",
              "      a.click();\n",
              "      div.remove();\n",
              "    }\n",
              "  "
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ],
            "application/javascript": [
              "download(\"download_c6889360-3674-4261-b392-675819f04923\", \"sales_by_aisle.csv\", 240)"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import files\n",
        "\n",
        "csv_files = [\n",
        "    \"sales_by_store.csv\"\n",
        "]\n",
        "\n",
        "for file in csv_files:\n",
        "    files.download(f\"/root/airflow/data/{file}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 17
        },
        "id": "Fc1WML6eH0Im",
        "outputId": "34d6d23d-9558-48e2-862c-f4f90ae2f405"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ],
            "application/javascript": [
              "\n",
              "    async function download(id, filename, size) {\n",
              "      if (!google.colab.kernel.accessAllowed) {\n",
              "        return;\n",
              "      }\n",
              "      const div = document.createElement('div');\n",
              "      const label = document.createElement('label');\n",
              "      label.textContent = `Downloading \"${filename}\": `;\n",
              "      div.appendChild(label);\n",
              "      const progress = document.createElement('progress');\n",
              "      progress.max = size;\n",
              "      div.appendChild(progress);\n",
              "      document.body.appendChild(div);\n",
              "\n",
              "      const buffers = [];\n",
              "      let downloaded = 0;\n",
              "\n",
              "      const channel = await google.colab.kernel.comms.open(id);\n",
              "      // Send a message to notify the kernel that we're ready.\n",
              "      channel.send({})\n",
              "\n",
              "      for await (const message of channel.messages) {\n",
              "        // Send a message to notify the kernel that we're ready.\n",
              "        channel.send({})\n",
              "        if (message.buffers) {\n",
              "          for (const buffer of message.buffers) {\n",
              "            buffers.push(buffer);\n",
              "            downloaded += buffer.byteLength;\n",
              "            progress.value = downloaded;\n",
              "          }\n",
              "        }\n",
              "      }\n",
              "      const blob = new Blob(buffers, {type: 'application/binary'});\n",
              "      const a = document.createElement('a');\n",
              "      a.href = window.URL.createObjectURL(blob);\n",
              "      a.download = filename;\n",
              "      div.appendChild(a);\n",
              "      a.click();\n",
              "      div.remove();\n",
              "    }\n",
              "  "
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ],
            "application/javascript": [
              "download(\"download_ba6c7167-aaf2-49b2-aea3-5ae3a182099c\", \"sales_by_store.csv\", 253)"
            ]
          },
          "metadata": {}
        }
      ]
    }
  ]
}
