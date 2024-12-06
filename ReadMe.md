1. 项目根目录

README.md：项目概述及如何开始。

requirements.txt：项目依赖库。

setup.py：用于安装项目的脚本。

.gitignore：Git忽略文件列表。

2. src （源代码目录）

2.1 screenshot_module/

screenshot.py：实现高频截图功能，包括窗口定位、截图频率控制。

window_utils.py：辅助工具函数，用于窗口获取和管理。

2.2 annotation_module/

manual_annotation_tool/：用于手工标注的工具集成（如使用LabelImg的脚本）。

annotation_preprocess.py：预处理图像并为标注做准备。

2.3 training_module/

train_model.py：深度学习模型的训练主脚本。

data_loader.py：数据加载和预处理工具。

model/：

crnn.py：CRNN模型定义。

east.py：EAST文本检测模型定义。

utils.py：训练过程中使用的工具函数（如数据增强、超参数调整）。

2.4 recognition_module/

recognize_text.py：对截图进行文字识别。

ctc_decoder.py：CTC解码实现。

preprocess.py：图像预处理和特征提取函数。

3. data （数据目录）

3.1 raw_screenshots/

存储高频截图的原始图像，以时间戳命名。

3.2 annotations/

手工标注数据，保存为XML或JSON格式。

3.3 datasets/

用于训练和验证的处理过的数据集。

train/：训练集数据。

val/：验证集数据。

4. models （模型目录）

saved_models/：保存训练好的深度学习模型。

checkpoints/：模型训练过程中保存的检查点。

5. tests （测试目录）

5.1 unit_tests/

针对各模块的单元测试。

test_screenshot.py：截图模块的测试脚本。

test_annotation.py：标注模块的测试脚本。

5.2 integration_tests/

集成测试脚本，验证各模块的协作情况。

test_integration.py：整体系统的集成测试。

6. scripts （脚本目录）

deploy.sh：自动化部署脚本。

run_inference.py：用于执行推理的脚本。

evaluate_performance.py：评估系统性能的脚本。

7. docs （文档目录）

7.1 design_docs/

系统架构设计文档。

各模块的详细设计描述。

7.2 user_manual/

用户手册：如何运行、使用和维护该系统。

FAQ和常见问题解答。

8. logs （日志目录）

screenshot_logs/：存储截图模块的日志。

training_logs/：训练过程中产生的日志，用于分析训练效果。

inference_logs/：文字识别模块的运行日志。

9. configs （配置文件目录）

config.yaml：系统整体配置文件，包括路径、训练参数等。

logging_config.yaml：日志系统配置。

10. notebooks （Jupyter笔记本目录）

exploratory_analysis.ipynb：用于数据探索和初步分析的笔记本。

model_tuning.ipynb：用于超参数调整和模型调优。

11. 维护与扩展

11.1 日常运维

maintenance/：

monitoring.py：系统监控脚本。

cleanup.py：清理无用文件和数据的脚本。

11.2 扩展开发

未来扩展功能的开发脚本和实验代码。

12. 附录

12.1 参考文献

列出所有用到的书籍、论文、技术文档等。

12.2 常见问题

系统开发、部署过程中可能遇到的问题及其解决方案。