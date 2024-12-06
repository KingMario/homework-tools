# PDF 作业工具

## 介绍

在为您的孩子准备作业时，有时作业会包含参考答案。如果参考答案在新的一页上，您可以简单地打印答案页之前的页面。然而，如果参考答案不是从页面的开头开始，您需要在打印之前覆盖页面上的答案。仅仅覆盖答案可能无法完全满足打印答案的需求。

## 解决方案

对于（部分）作业和（部分）答案在同一页的情况，您可以复制页面并分别覆盖答案和作业部分，以获得可以分别打印的页面。

解决方案分为手动和自动方法。

### 手动方法

指定 PDF 文档路径、页码以及需要从底部向上覆盖的页面比例。

### 自动方法

指定要搜索的目标文本（例如，“参考答案”），然后自动搜索包含目标文本的页面，通过检查找到最佳覆盖比例，并以与手动方法相同的方式处理。

您还可以使用环境变量 `APHP_TARGET_TEXT` 设置目标文本。

使用环境变量 `APHP_TARGET_TEXT` 的好处是，对于目标文本相同的多个 PDF 文档，可以简化命令。

## 脚本

### `prepare_homework_pdf.py`

此脚本允许您手动指定 PDF 文档路径、页码以及需要从底部向上覆盖的页面比例。

### `auto_prepare_homework_pdf.py`

此脚本允许您指定要搜索的目标文本，自动找到包含目标文本的页面，确定最佳覆盖比例，并相应地处理页面。

## 用法

### 手动方法

```bash
python prepare_homework_pdf.py <pdf_path> <page_number> <cover_ratio>
```

### 自动方法

```bash
python auto_prepare_homework_pdf.py <pdf_path> <target_text>
```

或者，您可以使用环境变量 `APHP_TARGET_TEXT` 设置目标文本：

```bash
export APHP_TARGET_TEXT="参考答案"
python auto_prepare_homework_pdf.py <pdf_path>
```

## 要求

- Python 3.x
- PyMuPDF

使用以下命令安装所需的包：

```bash
pip install PyMuPDF
```

## 许可证

此项目根据 MIT 许可证授权。