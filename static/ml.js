document.addEventListener('DOMContentLoaded', function () {
    var form = document.getElementById('mlForm');
    var resultContainer = document.getElementById('resultContainer');

    function submitForm(formDataObject) {
        fetch('http://127.0.0.1:5000/predict_proficiency', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formDataObject),
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            var predictedLevel = data.predicted_level;
            resultContainer.innerHTML = 'You are ' + predictedLevel + ' in Machine Learning!!!';
        })
        .catch(error => console.error('Error:', error));
    }

    form.addEventListener('submit', function (event) {
        event.preventDefault();

        var formDataObject = {
            'q1_yes': mapRadioValue('optionsRadios1'),
            'q2_yes': mapRadioValue('optionsRadios2'),
            'q3_yes': mapRadioValue('optionsRadios3'),
            'q4_yes': mapRadioValue('optionsRadios4'),
            'q5_yes': mapRadioValue('optionsRadios5'),
        };

        submitForm(formDataObject);
    });

    function mapRadioValue(name) {
        var value = getRadioValue(name);
        if (value === 'option1') {
            return 'Yes';
        } else if (value === 'option2') {
            return 'No';
        } else if (value === 'option3') {
            return 'Not Sure';
        }
        return null;
    }

    function getRadioValue(name) {
        var radios = form.elements[name];
        for (var i = 0; i < radios.length; i++) {
            if (radios[i].checked) {
                return radios[i].value;
            }
        }
        return null;
    }

    function resetForm() {
        var radioButtons = form.querySelectorAll('input[type="radio"]');
        radioButtons.forEach(function (radioButton) {
            radioButton.checked = false;
        });
    
        resultContainer.innerHTML = '';
    }
    var resetButton = form.querySelector('button[type="reset"]');
    resetButton.addEventListener('click', resetForm);
    
    function toggleNavbar() {
        var navbarCollapse = document.getElementById('navbarColor01');
        if (navbarCollapse.style.display === 'none' || navbarCollapse.style.display === '') {
            navbarCollapse.style.display = 'block';
        } else {
            navbarCollapse.style.display = 'none';
        }
    }
});
