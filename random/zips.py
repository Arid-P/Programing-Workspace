from zipfile import ZipFile
from base_pathlib import Path
import os
from icecream import ic


# =========================
# CONSTANTS
# =========================

SOURCE_DIR = Path('../../Documents/test')

ZIP_PREFIX_CLASS_11 = {
    'keph': "Physics",
    'kech': "Chemistry",
    'kemh': "Mathematics",
    'x': "English",
    'y': "Computer Science"
}

ZIP_PREFIX_CLASS_12 = {
    's': "Physics",
    'g': "Chemistry",
    'h': "Mathematics",
    'x': "English",
    'y': "Computer Science"
}


# =========================
# CHAPTER DATA
# =========================

CHAPTERS_CLASS_11= {
    "Physics" : [
    "Units and Measurements",
    "Motion in a Straight Line",
    "Motion in a Plane",
    "Laws of Motion",
    "Work, Energy and Power",
    "System of Particles and Rotational Motion",
    "Gravitation",
    "Mechanical Properties of Solids",
    "Mechanical Properties of Fluids",
    "Thermal Properties of Matter",
    "Thermodynamics",
    "Kinetic Theory",
    "Oscillations",
    "Waves"
],

    "Chemistry" : [
    "Some Basic Concepts of Chemistry",
    "Structure of Atom",
    "Classification of Elements and Periodicity in Properties",
    "Chemical Bonding and Molecular Structure",
    "Chemical Thermodynamics",
    "Equilibrium",
    "Redox Reactions",
    "Organic Chemistry, Some Basic Principles and Techniques",
    "Hydrocarbons"
],

    "Mathematics" : [
    "Sets",
    "Relations and Functions",
    "Trigonometric Functions",
    "Complex Numbers and Quadratic Equations",
    "Linear Inequalities",
    "Permutations and Combinations",
    "Binomial Theorem",
    "Sequences and Series",
    "Straight Lines",
    "Conic Sections",
    "Introduction to Three-Dimensional Geometry",
    "Limits and Derivatives",
    "Statistics",
    "Probability"
],
}
CHAPTERS_CLASS_12 = {
    "Physics": [
        "Electric Charges and Fields",
        "Electrostatic Potential and Capacitance",
        "Current Electricity",
        "Moving Charges and Magnetism",
        "Magnetism and Matter",
        "Electromagnetic Induction",
        "Alternating Current",
        "Electromagnetic Waves",
        "Ray Optics and Optical Instruments",
        "Wave Optics",
        "Dual Nature of Radiation and Matter",
        "Atoms",
        "Nuclei",
        "Semiconductor Electronics, Materials, Devices and Simple Circuits"
    ],

    "Chemistry": [
        "Solutions",
        "Electrochemistry",
        "Chemical Kinetics",
        "The d- and f-Block Elements",
        "Coordination Compounds",
        "Haloalkanes and Haloarenes",
        "Alcohols, Phenols and Ethers",
        "Aldehydes, Ketones and Carboxylic Acids",
        "Amines",
        "Biomolecules"
    ],

    "Mathematics": [
        "Relations and Functions",
        "Inverse Trigonometric Functions",
        "Matrices",
        "Determinants",
        "Continuity and Differentiability",
        "Applications of Derivatives",
        "Integrals",
        "Applications of Integrals",
        "Differential Equations",
        "Vector Algebra",
        "Three-Dimensional Geometry",
        "Linear Programming",
        "Probability"
    ]
}

# =========================
# UTILITIES
# =========================

def error_guard(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            ic(e)
    return wrapper

def pause_debug(msg: str = ''):
    items = sorted(os.listdir())
    print()
    ic(msg, items) if msg else ic(items)
    print()
    input("continue?")


# =========================
# RENAMING SPECIAL FILES
# =========================

@error_guard
def rename_special_sections():
    cycle = 1

    # runs twice (two zip parts)
    while cycle <= 2:
        content = sorted(os.listdir())

        @error_guard
        def rename_preface():
            file_ = list(filter(lambda f: 'ps' in f, content))
            os.rename(file_[0], f"{cycle}_Preface.pdf")
        @error_guard
        def rename_answers():
            file_ = list(filter(lambda f: 'an' in f, content))
            os.rename(file_[0], f"z{cycle}_Answer.pdf")
        @error_guard
        def rename_appendix():
            file_ = list(filter(lambda f: f'a{cycle}' in f, content))
            os.rename(file_[0], f"x{cycle}_Appendix.pdf")
        @error_guard
        def rename_supplement():
            file_ = list(filter(lambda f: 'sm' in f, content))
            os.rename(file_[0], f"y{cycle}_Supplementary.pdf")
            
        rename_preface()
        rename_answers()
        rename_appendix()
        rename_supplement()
        
        cycle += 1
        return


# =========================
# CHAPTER RENAMING
# =========================

@error_guard
def rename_chapters(zip_prefix, subject, class_no):

    pause_debug("Calling special renaming")
    rename_special_sections()

    content = sorted(os.listdir())
    pause_debug("Before chapter rename")

    chapters = list(filter(lambda f: zip_prefix in f, content))

    if class_no == 11:
        names = CHAPTERS_CLASS_11[subject]
    else:
        names = CHAPTERS_CLASS_12[subject]

    for index, file_name in enumerate(chapters, start=1):

        number_prefix = f"0{index}_" if index < 10 else f"{index}_"
        new_name = f"{number_prefix}{names[index - 1]}.pdf"

        os.rename(file_name, new_name)

    pause_debug("After chapter rename")
    return


# =========================
# CLASS PROCESSOR
# =========================

def process_class(class_no: int):
    return_path = Path(*['..'] * 2)

    zip_map = (
        ZIP_PREFIX_CLASS_11
        if class_no == 11
        else ZIP_PREFIX_CLASS_12
    )

    for zip_prefix, subject in zip_map.items():
        folder = Path(subject, f"Class {class_no}")
        
        # create folder if missing
        folder.mkdir(parents=True, exist_ok=True)

        # skip if already processed
        if any(folder.iterdir()):
            continue

        # extract both zip parts
        for part in range(1, 3):
            try:
                zip_path = Path(SOURCE_DIR, f"{zip_prefix}{part}dd.zip")
                zip_file = ZipFile(zip_path, 'r')
            except Exception as e:
                ic(e)
                continue
            
            ic(f"Extracting {subject}")
            zip_file.extractall(path=folder)
            zip_file.close()
            ic("Extraction completed")
            
        os.chdir(folder)
        rename_chapters(zip_prefix, subject, class_no)
        os.chdir(return_path)
        return


# =========================
# ENTRY POINT
# =========================

def main():
    process_class(11)
    process_class(12)
    return


if __name__ == "__main__":
    os.chdir(SOURCE_DIR)
    main()